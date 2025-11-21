"""
Blender Import Script for Apartment E.1.5.47

This script automatically imports the apartment 3D model into Blender and sets up:
- Proper materials with colors
- Lighting setup
- Camera views
- Scene organization

USAGE:
1. Open Blender
2. Go to Scripting workspace
3. Open this file or paste the code
4. Update the BASE_PATH variable to your project location
5. Run the script (Alt+P or click Run Script button)

Requirements: Blender 2.8 or newer
"""

import bpy
import json
import os
from pathlib import Path
from math import radians

# ============================================
# CONFIGURATION
# ============================================

# UPDATE THIS PATH to your project directory
BASE_PATH = "/home/user/construction-planning"

# File paths
JSON_PATH = os.path.join(BASE_PATH, "output/json/apartment_data.json")
OBJ_PATH = os.path.join(BASE_PATH, "output/obj/apartment.obj")
GLTF_PATH = os.path.join(BASE_PATH, "output/gltf/apartment.gltf")

# Choose import format: "OBJ" or "GLTF"
IMPORT_FORMAT = "OBJ"

# ============================================
# UTILITY FUNCTIONS
# ============================================

def clear_scene():
    """Clear all objects, materials, and lights from the scene"""
    print("Clearing scene...")

    # Delete all objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Delete all materials
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

    # Delete all lights
    for light in bpy.data.lights:
        bpy.data.lights.remove(light)

    # Delete all cameras
    for camera in bpy.data.cameras:
        bpy.data.cameras.remove(camera)

    print("✓ Scene cleared")

def load_apartment_data():
    """Load apartment data from JSON"""
    print(f"Loading apartment data from: {JSON_PATH}")

    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✓ Apartment data loaded")
        return data
    except FileNotFoundError:
        print(f"⚠ JSON file not found: {JSON_PATH}")
        return None

def import_model():
    """Import the 3D model"""
    print(f"Importing {IMPORT_FORMAT} model...")

    if IMPORT_FORMAT == "OBJ":
        if not os.path.exists(OBJ_PATH):
            print(f"⚠ OBJ file not found: {OBJ_PATH}")
            return None

        # Import OBJ
        bpy.ops.import_scene.obj(filepath=OBJ_PATH)
        print("✓ OBJ model imported")

    elif IMPORT_FORMAT == "GLTF":
        if not os.path.exists(GLTF_PATH):
            print(f"⚠ glTF file not found: {GLTF_PATH}")
            return None

        # Import glTF
        bpy.ops.import_scene.gltf(filepath=GLTF_PATH)
        print("✓ glTF model imported")

    return bpy.context.selected_objects

def create_materials():
    """Create and assign materials to objects"""
    print("Creating materials...")

    # Material definitions
    materials = {
        'walls': {
            'color': (0.9, 0.9, 0.85, 1.0),
            'roughness': 0.7,
            'metallic': 0.0
        },
        'floor': {
            'color': (0.7, 0.6, 0.5, 1.0),
            'roughness': 0.6,
            'metallic': 0.0
        },
        'ceiling': {
            'color': (1.0, 1.0, 1.0, 1.0),
            'roughness': 0.8,
            'metallic': 0.0
        }
    }

    created_materials = {}

    for mat_name, props in materials.items():
        # Create material
        mat = bpy.data.materials.new(name=mat_name)
        mat.use_nodes = True

        # Get the principled BSDF node
        bsdf = mat.node_tree.nodes.get('Principled BSDF')
        if bsdf:
            bsdf.inputs['Base Color'].default_value = props['color']
            bsdf.inputs['Roughness'].default_value = props['roughness']
            bsdf.inputs['Metallic'].default_value = props['metallic']

        created_materials[mat_name] = mat
        print(f"  ✓ Created material: {mat_name}")

    # Assign materials to objects based on name
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # Clear existing materials
            obj.data.materials.clear()

            # Assign based on object name or position
            obj_name_lower = obj.name.lower()
            if 'floor' in obj_name_lower:
                obj.data.materials.append(created_materials['floor'])
            elif 'ceiling' in obj_name_lower:
                obj.data.materials.append(created_materials['ceiling'])
            elif 'wall' in obj_name_lower:
                obj.data.materials.append(created_materials['walls'])
            else:
                # Default to walls
                obj.data.materials.append(created_materials['walls'])

    print("✓ Materials created and assigned")
    return created_materials

def setup_lighting(data):
    """Setup lighting for the scene"""
    print("Setting up lighting...")

    dims = data['apartment']['dimensions']
    center_x = dims['approximateWidth'] / 2
    center_y = dims['approximateDepth'] / 2
    ceiling_height = dims['ceilingHeight']

    # Sun light (global illumination)
    bpy.ops.object.light_add(type='SUN', location=(center_x, center_y, ceiling_height + 5))
    sun = bpy.context.active_object
    sun.name = "Sun"
    sun.rotation_euler = (radians(45), radians(45), 0)
    sun.data.energy = 3.0
    sun.data.color = (1.0, 0.98, 0.95)
    print("  ✓ Sun light added")

    # Area light (room light)
    bpy.ops.object.light_add(type='AREA', location=(center_x, center_y, ceiling_height - 0.3))
    area = bpy.context.active_object
    area.name = "Ceiling Light"
    area.data.energy = 200
    area.data.size = 2.0
    area.data.color = (1.0, 0.95, 0.9)
    print("  ✓ Area light added")

    # Additional point lights for better illumination
    positions = [
        (center_x - 2, center_y - 4, ceiling_height - 0.5),
        (center_x + 2, center_y + 4, ceiling_height - 0.5),
    ]

    for i, pos in enumerate(positions):
        bpy.ops.object.light_add(type='POINT', location=pos)
        point = bpy.context.active_object
        point.name = f"Point Light {i+1}"
        point.data.energy = 100
        point.data.color = (1.0, 0.95, 0.9)

    print(f"  ✓ Added {len(positions)} point lights")
    print("✓ Lighting setup complete")

def setup_cameras(data):
    """Setup camera views"""
    print("Setting up cameras...")

    dims = data['apartment']['dimensions']
    center_x = dims['approximateWidth'] / 2
    center_y = dims['approximateDepth'] / 2
    ceiling_height = dims['ceilingHeight']

    # Camera 1: Overview (isometric-style)
    bpy.ops.object.camera_add(location=(center_x + 8, center_y - 10, ceiling_height + 6))
    cam1 = bpy.context.active_object
    cam1.name = "Camera_Overview"
    cam1.rotation_euler = (radians(60), 0, radians(45))
    print("  ✓ Overview camera added")

    # Camera 2: Top-down view
    bpy.ops.object.camera_add(location=(center_x, center_y, ceiling_height + 8))
    cam2 = bpy.context.active_object
    cam2.name = "Camera_TopDown"
    cam2.rotation_euler = (0, 0, 0)
    print("  ✓ Top-down camera added")

    # Camera 3: Interior view (living room)
    bpy.ops.object.camera_add(location=(center_x, center_y + 6, 1.6))
    cam3 = bpy.context.active_object
    cam3.name = "Camera_Interior"
    cam3.rotation_euler = (radians(90), 0, radians(180))
    print("  ✓ Interior camera added")

    # Set the first camera as active
    bpy.context.scene.camera = cam1

    print("✓ Cameras setup complete")

def organize_scene():
    """Organize objects into collections"""
    print("Organizing scene...")

    # Create collections
    collections = {}
    collection_names = ['Geometry', 'Lights', 'Cameras']

    for col_name in collection_names:
        if col_name not in bpy.data.collections:
            col = bpy.data.collections.new(col_name)
            bpy.context.scene.collection.children.link(col)
            collections[col_name] = col
        else:
            collections[col_name] = bpy.data.collections[col_name]

    # Move objects to appropriate collections
    for obj in bpy.data.objects:
        # Unlink from current collections
        for col in obj.users_collection:
            col.objects.unlink(obj)

        # Link to appropriate collection
        if obj.type == 'MESH':
            collections['Geometry'].objects.link(obj)
        elif obj.type == 'LIGHT':
            collections['Lights'].objects.link(obj)
        elif obj.type == 'CAMERA':
            collections['Cameras'].objects.link(obj)

    print("✓ Scene organized into collections")

def setup_render_settings(data):
    """Configure render settings"""
    print("Configuring render settings...")

    scene = bpy.context.scene

    # Use Cycles for better quality (or Eevee for speed)
    scene.render.engine = 'CYCLES'  # Change to 'BLENDER_EEVEE' for faster preview

    # Render resolution
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100

    # Cycles settings
    scene.cycles.samples = 128  # Increase for better quality
    scene.cycles.use_denoising = True

    # World background
    world = bpy.data.worlds.get('World')
    if world:
        world.use_nodes = True
        bg_node = world.node_tree.nodes.get('Background')
        if bg_node:
            bg_node.inputs['Color'].default_value = (0.8, 0.85, 0.9, 1.0)
            bg_node.inputs['Strength'].default_value = 0.5

    print("✓ Render settings configured")

def add_text_info(data):
    """Add text object with apartment information"""
    print("Adding information text...")

    apt = data['apartment']
    metadata = apt['metadata']

    # Create text
    bpy.ops.object.text_add(location=(0, 0, 0))
    text_obj = bpy.context.active_object
    text_obj.name = "Apartment_Info"

    # Set text content
    info_text = f"""Apartment: {metadata['id']}
Floor: {metadata['floor']}
Area: {metadata['totalUsableArea']} m²
Rooms: {len(apt['rooms'])}
Developer: {metadata['developer']}"""

    text_obj.data.body = info_text
    text_obj.data.size = 0.3
    text_obj.data.align_x = 'LEFT'

    # Position text to the side
    dims = apt['dimensions']
    text_obj.location = (dims['approximateWidth'] + 1, 0, 1)

    print("✓ Information text added")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("APARTMENT E.1.5.47 - BLENDER IMPORT SCRIPT")
    print("="*60 + "\n")

    # Load apartment data
    data = load_apartment_data()
    if not data:
        print("\n⚠ ERROR: Could not load apartment data")
        print("Please update the BASE_PATH variable in the script")
        return

    # Clear existing scene
    clear_scene()

    # Import 3D model
    imported_objects = import_model()
    if not imported_objects:
        print("\n⚠ ERROR: Could not import model")
        return

    # Setup materials
    create_materials()

    # Setup lighting
    setup_lighting(data)

    # Setup cameras
    setup_cameras(data)

    # Organize scene
    organize_scene()

    # Setup render settings
    setup_render_settings(data)

    # Add info text
    add_text_info(data)

    # Frame all objects in view
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.view3d.view_selected()

    print("\n" + "="*60)
    print("✓ IMPORT COMPLETE!")
    print("="*60)
    print("\nNext steps:")
    print("1. Switch to 'Shading' workspace to adjust materials")
    print("2. Switch between cameras using numpad 0")
    print("3. Render with F12")
    print("4. Use Collections panel to show/hide elements")
    print("\nTip: Change RENDER_ENGINE to 'BLENDER_EEVEE' for faster preview")
    print("="*60 + "\n")

# Run the script
if __name__ == "__main__":
    main()
