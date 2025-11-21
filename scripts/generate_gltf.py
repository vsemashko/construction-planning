#!/usr/bin/env python3
"""
Generate glTF 3D model from apartment JSON data
"""
import json
import struct
import base64
from pathlib import Path

class GLTFGenerator:
    def __init__(self):
        self.vertices = []
        self.indices = []

    def add_box(self, x1, y1, z1, x2, y2, z2):
        """Add a box to the mesh"""
        # 8 vertices of the box
        base_idx = len(self.vertices)
        box_vertices = [
            [x1, z1, y1], [x2, z1, y1], [x2, z1, y2], [x1, z1, y2],  # Bottom
            [x1, z2, y1], [x2, z2, y1], [x2, z2, y2], [x1, z2, y2],  # Top
        ]
        self.vertices.extend(box_vertices)

        # 12 triangles (2 per face, 6 faces)
        box_indices = [
            # Bottom
            0, 1, 2, 0, 2, 3,
            # Top
            4, 6, 5, 4, 7, 6,
            # Front
            0, 5, 1, 0, 4, 5,
            # Back
            2, 7, 3, 2, 6, 7,
            # Left
            0, 7, 4, 0, 3, 7,
            # Right
            1, 6, 2, 1, 5, 6,
        ]
        self.indices.extend([i + base_idx for i in box_indices])

    def generate_gltf(self, data):
        """Generate glTF JSON from apartment data"""
        apt = data['apartment']
        dims = apt['dimensions']

        # Generate geometry
        # Floor
        floor_thickness = 0.2
        self.add_box(
            0, 0, -floor_thickness,
            dims['approximateWidth'], dims['approximateDepth'], 0
        )

        # Walls
        for wall in apt['walls']:
            x1, y1 = wall['start']['x'], wall['start']['y']
            x2, y2 = wall['end']['x'], wall['end']['y']
            thickness = wall['thickness']
            height = wall['height']

            if abs(x2 - x1) > abs(y2 - y1):  # Horizontal wall
                self.add_box(
                    min(x1, x2), y1 - thickness/2, 0,
                    max(x1, x2), y1 + thickness/2, height
                )
            else:  # Vertical wall
                self.add_box(
                    x1 - thickness/2, min(y1, y2), 0,
                    x1 + thickness/2, max(y1, y2), height
                )

        # Ceiling
        ceiling_thickness = 0.2
        self.add_box(
            0, 0, dims['ceilingHeight'],
            dims['approximateWidth'], dims['approximateDepth'], dims['ceilingHeight'] + ceiling_thickness
        )

        # Convert vertices to binary buffer
        vertex_buffer = b''
        for v in self.vertices:
            vertex_buffer += struct.pack('fff', v[0], v[1], v[2])

        # Convert indices to binary buffer
        index_buffer = b''
        for i in self.indices:
            index_buffer += struct.pack('H', i)  # Unsigned short

        # Combine buffers
        combined_buffer = vertex_buffer + index_buffer

        # Calculate buffer views
        vertex_byte_length = len(vertex_buffer)
        index_byte_offset = vertex_byte_length
        index_byte_length = len(index_buffer)

        # Calculate bounding box
        xs = [v[0] for v in self.vertices]
        ys = [v[1] for v in self.vertices]
        zs = [v[2] for v in self.vertices]
        min_bounds = [min(xs), min(ys), min(zs)]
        max_bounds = [max(xs), max(ys), max(zs)]

        # Create glTF JSON structure
        gltf = {
            "asset": {
                "version": "2.0",
                "generator": "Python glTF Generator",
                "copyright": f"Apartment {apt['metadata']['id']}"
            },
            "scene": 0,
            "scenes": [
                {
                    "name": f"Apartment {apt['metadata']['id']}",
                    "nodes": [0]
                }
            ],
            "nodes": [
                {
                    "name": "Apartment",
                    "mesh": 0
                }
            ],
            "meshes": [
                {
                    "name": "Apartment Geometry",
                    "primitives": [
                        {
                            "attributes": {
                                "POSITION": 0
                            },
                            "indices": 1,
                            "material": 0
                        }
                    ]
                }
            ],
            "materials": [
                {
                    "name": "Apartment Material",
                    "pbrMetallicRoughness": {
                        "baseColorFactor": [0.9, 0.9, 0.9, 1.0],
                        "metallicFactor": 0.0,
                        "roughnessFactor": 0.8
                    }
                }
            ],
            "accessors": [
                {
                    "bufferView": 0,
                    "byteOffset": 0,
                    "componentType": 5126,  # FLOAT
                    "count": len(self.vertices),
                    "type": "VEC3",
                    "min": min_bounds,
                    "max": max_bounds
                },
                {
                    "bufferView": 1,
                    "byteOffset": 0,
                    "componentType": 5123,  # UNSIGNED_SHORT
                    "count": len(self.indices),
                    "type": "SCALAR"
                }
            ],
            "bufferViews": [
                {
                    "buffer": 0,
                    "byteOffset": 0,
                    "byteLength": vertex_byte_length,
                    "target": 34962  # ARRAY_BUFFER
                },
                {
                    "buffer": 0,
                    "byteOffset": index_byte_offset,
                    "byteLength": index_byte_length,
                    "target": 34963  # ELEMENT_ARRAY_BUFFER
                }
            ],
            "buffers": [
                {
                    "byteLength": len(combined_buffer),
                    "uri": f"data:application/octet-stream;base64,{base64.b64encode(combined_buffer).decode('utf-8')}"
                }
            ]
        }

        return gltf

def load_apartment_data(json_path):
    """Load apartment data from JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_gltf_model(data, output_path):
    """Create glTF 3D model from apartment data"""
    generator = GLTFGenerator()
    gltf = generator.generate_gltf(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(gltf, f, indent=2)

    print(f"✓ glTF 3D model generated: {output_path}")
    print(f"  Vertices: {len(generator.vertices)}")
    print(f"  Triangles: {len(generator.indices) // 3}")

if __name__ == '__main__':
    # Paths
    base_dir = Path(__file__).parent.parent
    json_path = base_dir / 'output' / 'json' / 'apartment_data.json'
    output_path = base_dir / 'output' / 'gltf' / 'apartment.gltf'

    # Generate glTF
    data = load_apartment_data(json_path)
    create_gltf_model(data, output_path)
