#!/usr/bin/env python3
"""
Generate OBJ 3D model from apartment JSON data
"""
import json
from pathlib import Path

class OBJGenerator:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.vertex_count = 1  # OBJ indices start at 1

    def add_vertex(self, x, y, z):
        """Add a vertex and return its index"""
        self.vertices.append(f"v {x:.3f} {y:.3f} {z:.3f}")
        idx = self.vertex_count
        self.vertex_count += 1
        return idx

    def add_face(self, v1, v2, v3, v4=None):
        """Add a face (triangle or quad)"""
        if v4:
            self.faces.append(f"f {v1} {v2} {v3} {v4}")
        else:
            self.faces.append(f"f {v1} {v2} {v3}")

    def create_box(self, x1, y1, z1, x2, y2, z2):
        """Create a box and return vertex indices"""
        # 8 vertices of the box
        v1 = self.add_vertex(x1, y1, z1)
        v2 = self.add_vertex(x2, y1, z1)
        v3 = self.add_vertex(x2, y2, z1)
        v4 = self.add_vertex(x1, y2, z1)
        v5 = self.add_vertex(x1, y1, z2)
        v6 = self.add_vertex(x2, y1, z2)
        v7 = self.add_vertex(x2, y2, z2)
        v8 = self.add_vertex(x1, y2, z2)

        # 6 faces (quads)
        self.add_face(v1, v2, v3, v4)  # Bottom
        self.add_face(v5, v6, v7, v8)  # Top
        self.add_face(v1, v2, v6, v5)  # Front
        self.add_face(v3, v4, v8, v7)  # Back
        self.add_face(v1, v4, v8, v5)  # Left
        self.add_face(v2, v3, v7, v6)  # Right

    def generate_obj(self, data):
        """Generate OBJ content from apartment data"""
        apt = data['apartment']
        dims = apt['dimensions']

        # Add comment header
        lines = [
            f"# Apartment {apt['metadata']['id']} - 3D Model",
            f"# Generated from architectural documents",
            f"# Total area: {apt['metadata']['totalUsableArea']} m²",
            f"# Ceiling height: {dims['ceilingHeight']} m",
            "",
            "# Material library (optional)",
            "mtllib apartment.mtl",
            ""
        ]

        # Generate floor
        lines.append("# Floor")
        lines.append("g floor")
        floor_thickness = 0.2
        self.create_box(
            0, 0, -floor_thickness,
            dims['approximateWidth'], dims['approximateDepth'], 0
        )

        # Generate walls
        lines.append("# Walls")
        lines.append("g walls")
        for wall in apt['walls']:
            x1, y1 = wall['start']['x'], wall['start']['y']
            x2, y2 = wall['end']['x'], wall['end']['y']
            thickness = wall['thickness']
            height = wall['height']

            # Determine wall orientation and create box
            if abs(x2 - x1) > abs(y2 - y1):  # Horizontal wall (along X)
                self.create_box(
                    min(x1, x2), y1 - thickness/2, 0,
                    max(x1, x2), y1 + thickness/2, height
                )
            else:  # Vertical wall (along Y)
                self.create_box(
                    x1 - thickness/2, min(y1, y2), 0,
                    x1 + thickness/2, max(y1, y2), height
                )

        # Generate ceiling
        lines.append("# Ceiling")
        lines.append("g ceiling")
        ceiling_thickness = 0.2
        self.create_box(
            0, 0, dims['ceilingHeight'],
            dims['approximateWidth'], dims['approximateDepth'], dims['ceilingHeight'] + ceiling_thickness
        )

        # Combine all vertices and faces
        lines.append("")
        lines.extend(self.vertices)
        lines.append("")
        lines.extend(self.faces)

        return '\n'.join(lines)

def load_apartment_data(json_path):
    """Load apartment data from JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_obj_model(data, output_path):
    """Create OBJ 3D model from apartment data"""
    generator = OBJGenerator()
    obj_content = generator.generate_obj(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(obj_content)

    print(f"✓ OBJ 3D model generated: {output_path}")
    print(f"  Vertices: {len(generator.vertices)}")
    print(f"  Faces: {len(generator.faces)}")

    # Also create a simple MTL file
    mtl_path = output_path.parent / 'apartment.mtl'
    mtl_content = """# Material library
newmtl walls
Ka 0.8 0.8 0.8
Kd 0.9 0.9 0.9
Ks 0.1 0.1 0.1
Ns 10

newmtl floor
Ka 0.7 0.6 0.5
Kd 0.8 0.7 0.6
Ks 0.2 0.2 0.2
Ns 20

newmtl ceiling
Ka 1.0 1.0 1.0
Kd 1.0 1.0 1.0
Ks 0.1 0.1 0.1
Ns 10
"""
    with open(mtl_path, 'w', encoding='utf-8') as f:
        f.write(mtl_content)
    print(f"✓ Material file generated: {mtl_path}")

if __name__ == '__main__':
    # Paths
    base_dir = Path(__file__).parent.parent
    json_path = base_dir / 'output' / 'json' / 'apartment_data.json'
    output_path = base_dir / 'output' / 'obj' / 'apartment.obj'

    # Generate OBJ
    data = load_apartment_data(json_path)
    create_obj_model(data, output_path)
