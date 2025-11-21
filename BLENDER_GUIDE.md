# Blender Import Guide - Apartment E.1.5.47

Complete guide for importing and working with the apartment 3D model in Blender.

---

## Table of Contents

1. [Quick Start - Automated Import](#quick-start---automated-import)
2. [Manual Import Methods](#manual-import-methods)
3. [Working in Blender](#working-in-blender)
4. [Interior Design Workflow](#interior-design-workflow)
5. [Rendering](#rendering)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start - Automated Import

### Method 1: Using the Python Script (Recommended)

The fastest way to get started is using our automated import script.

**Steps:**

1. **Download Blender** (if you don't have it)
   - Visit: https://www.blender.org/download/
   - Free and open-source
   - Requires Blender 2.8 or newer

2. **Open Blender**
   - Start a new project (General template)

3. **Open the Script**
   - Click on "Scripting" workspace at the top
   - Click "Open" button or go to Text → Open
   - Navigate to `scripts/blender_import.py`

4. **Update the Path**
   - Find the line: `BASE_PATH = "/home/user/construction-planning"`
   - Change it to your actual project path
   - For Windows: `BASE_PATH = "C:/Users/YourName/construction-planning"`
   - For Mac: `BASE_PATH = "/Users/YourName/construction-planning"`

5. **Run the Script**
   - Press `Alt+P` or click the "Run Script" button (▶ icon)
   - Wait for the import to complete

6. **Done!**
   - Your apartment is now fully set up with:
     - ✅ Proper materials and colors
     - ✅ Multiple camera angles
     - ✅ Professional lighting
     - ✅ Organized collections
     - ✅ Render settings configured

**What the Script Does:**

- Imports the 3D model (OBJ or glTF)
- Creates realistic materials:
  - Walls: Light beige with slight roughness
  - Floor: Warm wood tone
  - Ceiling: White matte
- Sets up 3 cameras:
  - Overview (isometric view)
  - Top-down (floor plan view)
  - Interior (first-person view)
- Adds professional lighting:
  - Sun light for global illumination
  - Area lights for room ambience
  - Point lights for detail
- Organizes everything into collections
- Configures render settings (1920x1080, Cycles)
- Adds apartment information text

---

## Manual Import Methods

If you prefer to import manually or want more control:

### Method A: Import OBJ File

**Best for:** Traditional 3D workflow, maximum compatibility

1. **Open Blender** → New General project

2. **Delete Default Objects** (optional)
   - Select all: `A`
   - Delete: `X` → Delete

3. **Import OBJ**
   - File → Import → Wavefront (.obj)
   - Navigate to: `output/obj/apartment.obj`
   - Click "Import OBJ"

4. **Verify Import**
   - You should see walls, floor, and ceiling
   - Materials are automatically loaded from the .mtl file

5. **Frame the Model**
   - Press numpad `.` (period) to frame all objects
   - Or: View → Frame All

**OBJ Import Settings:**
- ✅ Split by Object
- ✅ Import Materials (MTL)
- Scale: 1.0 (already in meters)
- Forward: -Z Forward
- Up: Y Up

---

### Method B: Import glTF File

**Best for:** Modern workflow, web-compatible models

1. **Open Blender** → New General project

2. **Import glTF**
   - File → Import → glTF 2.0 (.gltf/.glb)
   - Navigate to: `output/gltf/apartment.gltf`
   - Click "Import glTF 2.0"

3. **Verify Import**
   - Model should appear with materials
   - glTF uses PBR materials (Metallic/Roughness)

**glTF Import Settings:**
- ✅ Remember Bone Dir
- ✅ Import Shading: Smooth

---

## Working in Blender

### Essential Blender Shortcuts

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Navigation** |
| Orbit View | Middle Mouse Drag | Rotate around model |
| Pan View | Shift + Middle Mouse | Move view |
| Zoom | Scroll Wheel | Zoom in/out |
| Frame All | Numpad `.` | Fit all objects in view |
| Front View | Numpad `1` | Orthographic front |
| Top View | Numpad `7` | Orthographic top |
| Camera View | Numpad `0` | View through camera |
| **Selection** |
| Select All | `A` | Select everything |
| Deselect All | Alt + `A` | Deselect everything |
| Box Select | `B` | Select area |
| **Objects** |
| Move | `G` | Grab/move object |
| Rotate | `R` | Rotate object |
| Scale | `S` | Scale object |
| Delete | `X` | Delete selected |
| **Rendering** |
| Render Image | `F12` | Render current view |
| Render Animation | Ctrl + `F12` | Render animation |

### Workspaces

Blender has different workspaces for different tasks:

1. **Modeling** - For editing geometry
2. **Shading** - For materials and textures
3. **Layout** - General purpose
4. **Rendering** - Set up renders

Switch between them using the tabs at the top.

---

## Interior Design Workflow

### Step 1: Orient Yourself

```
1. Press Numpad 0 to enter camera view
2. Press Numpad 7 for top-down view
3. Press Numpad 1 for front view
4. Use middle mouse to orbit freely
```

### Step 2: Add Furniture

**Option A: Import 3D Models**

Many free furniture models available:

- **Blender Add-ons:**
  - Asset Browser (built-in, Edit → Preferences → Add-ons → enable "Asset Browser")

- **Free Resources:**
  - BlendSwap.com
  - Sketchfab.com (many have free downloads)
  - Free3D.com
  - TurboSquid (has free section)

**Import Process:**
1. File → Append or Link
2. Navigate to .blend file
3. Select Object → Choose furniture
4. Place with `G` (move), `R` (rotate), `S` (scale)

**Option B: Create Simple Furniture**

```blender
# Add a cube (for table, bed, etc.)
Shift + A → Mesh → Cube

# Scale to desired size
S → type scale factor → Enter

# Move to position
G → Move mouse → Click to place
```

### Step 3: Improve Materials

1. **Switch to Shading Workspace**

2. **Select a Surface** (click on wall, floor, etc.)

3. **Edit Material in Shader Editor** (bottom panel)
   - Adjust "Base Color" for different colors
   - Change "Roughness" (0 = shiny, 1 = matte)
   - Add textures by clicking the dot next to Base Color

**Example: Wood Floor**

```
1. Select floor object
2. In Shader Editor: Principled BSDF node
3. Base Color → Add Image Texture
4. Download wood texture (free from Textures.com)
5. Adjust scale with Mapping node
```

**Example: Paint Walls**

```
1. Select wall
2. Change Base Color to desired paint color
3. Set Roughness to 0.6-0.8 for matte paint
```

### Step 4: Add Details

**Windows:**
- Add glass material to window areas
- Base Color: Light blue tint (0.8, 0.9, 1.0)
- Transmission: 0.95
- Roughness: 0.05

**Doors:**
- Add separate door objects
- Use brown/wood materials
- Add door handles

**Fixtures:**
- Light fixtures on ceiling
- Outlets on walls (from electrical plan)
- Radiators (positions from heating plan)

### Step 5: Lighting Enhancement

**Natural Light (Windows):**
```
Add → Light → Area
Position near window
Set color to daylight (0.9, 0.95, 1.0)
Set strength: 100-200W
```

**Artificial Light (Ceiling):**
```
Add → Light → Point or Spot
Position on ceiling
Set color to warm white (1.0, 0.95, 0.9)
Set strength: 100-150W
```

**Ambient Occlusion:**
```
Render Properties → Ambient Occlusion → Enable
Gives more realistic shadows in corners
```

---

## Rendering

### Quick Render Setup

1. **Choose Render Engine**
   - Render Properties tab (camera icon)
   - Engine: Cycles (better quality) or Eevee (faster)

2. **Set Resolution**
   - Output Properties (printer icon)
   - Resolution X: 1920, Y: 1080 (Full HD)
   - Or 3840 x 2160 (4K)

3. **Position Camera**
   - Select camera (click on it)
   - Press Numpad 0 to see camera view
   - `G` to move camera
   - `R` to rotate camera
   - Use camera view to compose your shot

4. **Render**
   - Press `F12` to render
   - Wait for completion
   - Image → Save As to save the render

### Render Settings by Purpose

**Quick Preview (Fast):**
```
Engine: Eevee
Samples: 64
Resolution: 1280x720
Estimated time: 5-10 seconds
```

**Good Quality (Medium):**
```
Engine: Cycles
Samples: 128
Resolution: 1920x1080
Denoising: On
Estimated time: 1-5 minutes
```

**Final Presentation (Slow):**
```
Engine: Cycles
Samples: 512-1024
Resolution: 3840x2160
Denoising: On
Light Path bounces: 12
Estimated time: 10-60 minutes
```

### Multiple Views Rendering

**Create a Turntable:**

1. Set up camera in good position
2. Timeline: Set end frame to 120 (for 5-second video at 24fps)
3. Frame 1: Select camera → `I` → Rotation
4. Frame 120: Rotate camera 360° → `I` → Rotation
5. Render → Render Animation (Ctrl+F12)

**Floor Plan Render:**

1. Switch to Camera_TopDown (if you used the script)
2. Or position camera directly above apartment
3. Camera Properties → Orthographic projection
4. Adjust Orthographic Scale to fit apartment
5. Render

---

## Advanced Techniques

### Add Realistic Textures

**Free Texture Sources:**
- Textures.com (formerly CG Textures)
- Poly Haven (polyhaven.com)
- AmbientCG (ambientcg.com)

**Apply Texture:**
1. Download texture (e.g., wood_floor.jpg)
2. Shading workspace
3. Add → Texture → Image Texture
4. Connect to Base Color
5. Open the image file

### Create Floor Plan Overlay

```python
# Run this in Blender's scripting tab
import bpy

# Add plane for floor plan overlay
bpy.ops.mesh.primitive_plane_add(size=10, location=(3.25, 7, 0.01))
plane = bpy.context.active_object

# Create material with SVG as texture
mat = bpy.data.materials.new("FloorPlan")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get('Principled BSDF')

# Add image texture node
tex_node = nodes.new('ShaderNodeTexImage')
# Load your SVG (converted to PNG first)
# tex_node.image = bpy.data.images.load("path/to/floor_plan.png")

plane.data.materials.append(mat)
```

### Export Renders for Presentation

**Best Formats:**

| Purpose | Format | Settings |
|---------|--------|----------|
| Print | PNG | RGBA, 16-bit, 300 DPI equivalent |
| Web | JPEG | 90% quality, sRGB |
| Editing | EXR | 32-bit float, all passes |
| Presentation | PNG | RGBA, sRGB |

---

## Troubleshooting

### Problem: Model appears too small/large

**Solution:**
```
1. Select all objects: A
2. Scale: S → type scale (e.g., 10 for 10x larger)
3. Apply scale: Ctrl+A → Scale
```

### Problem: Materials look flat

**Solution:**
```
1. Switch to Rendered view: Z → Rendered Viewport Shading
2. Or use Material Preview: Z → Material Preview
3. Add lights if scene is dark
4. Enable Bloom in render settings for glow effect
```

### Problem: Render is too dark

**Solution:**
```
1. Increase light strength: Select lights → Light Properties → Power
2. Add more lights: Shift+A → Light
3. Increase world background: World Properties → Surface → Strength
4. Use HDRI environment: World → Surface → Environment Texture
```

### Problem: Render takes forever

**Solution:**
```
1. Switch to Eevee: Render Properties → Engine → Eevee
2. Reduce samples: Render Properties → Sampling → Render (try 64)
3. Reduce resolution: Output Properties → Resolution % (try 50%)
4. Enable Denoising: Render Properties → Denoising
```

### Problem: Script won't run - "Path not found"

**Solution:**
```
1. Edit the script
2. Update BASE_PATH to your actual project path
3. Use forward slashes even on Windows: "C:/Users/Name/Project"
4. Make sure the path exists and contains the output folder
```

### Problem: OBJ imports without materials

**Solution:**
```
1. Make sure apartment.mtl is in the same folder as apartment.obj
2. Re-import with "Import Materials" checked
3. Or manually assign materials in Shading workspace
```

---

## Tips & Best Practices

### Performance Tips

1. **Use Collections** - Organize objects into collections and hide what you're not working on
2. **Simplify While Working** - Lower viewport samples for faster navigation
3. **Save Often** - Ctrl+S frequently, Blender can crash with complex scenes
4. **Auto-save** - Enable in Edit → Preferences → Save & Load

### Design Tips

1. **Use Reference Images**
   - Add → Image → Reference
   - Import photos of furniture/rooms for inspiration
   - Position in 3D space as guides

2. **Measure Everything**
   - Use Blender's measurement tools
   - Edge length display: Overlay → Measurement → Edge Length
   - Verify room dimensions match specs

3. **Lighting is Key**
   - Good lighting = professional results
   - Use 3-point lighting for hero shots
   - Mix warm and cool lights for depth

4. **Camera Composition**
   - Rule of thirds
   - Eye-level height for realistic views (1.6m)
   - Slight angle is more interesting than straight-on

### Workflow Tips

1. **Start Simple** - Basic materials first, details later
2. **Work in Layers** - Complete one room before moving to next
3. **Save Versions** - File → Save As → Increment number (apartment_v01, v02, etc.)
4. **Render Tests** - Do low-quality test renders before final render

---

## Next Steps

### Learning Resources

**Official Blender Resources:**
- Blender Manual: https://docs.blender.org/manual/en/latest/
- Blender Fundamentals: https://www.youtube.com/playlist?list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6

**YouTube Tutorials:**
- Blender Guru (Andrew Price) - Beginner tutorials
- Grant Abbitt - Interior design focus
- CG Geek - Architectural visualization
- Polygon Runway - Quick tips

**Interior Design Specific:**
- "Blender Architecture" YouTube channel
- "Architectural Visualization" courses on Udemy
- CG Cookie - Interior design courses

### Recommended Add-ons

**Free:**
- **Archimesh** - Generate walls, doors, windows
- **ArchiPack** - Parametric architectural objects
- **Measuring Tools** - Advanced measurement
- **Node Wrangler** - Faster material editing (built-in, enable in preferences)

**Paid:**
- **Archipack Pro** - Professional architectural tools ($60)
- **Blender Kit** - Huge 3D asset library (subscription)
- **Real Lights IES** - Professional lighting profiles

---

## Export Options

Once you've designed your apartment, you can export for other uses:

### Export to Other Software

**For SketchUp:**
```
File → Export → COLLADA (.dae)
Open in SketchUp: File → Import → .dae
```

**For Unreal Engine / Unity:**
```
File → Export → FBX (.fbx)
Use in game engines
```

**For Web (Three.js):**
```
File → Export → glTF 2.0 (.glb)
Use in web applications
```

**For 3D Printing:**
```
File → Export → STL (.stl)
For 3D printing architectural models
```

---

## Conclusion

You now have everything you need to:
- ✅ Import the apartment into Blender
- ✅ Add furniture and details
- ✅ Create realistic materials
- ✅ Set up professional lighting
- ✅ Render beautiful images

**Remember:**
- Start with the automated script for fastest setup
- Experiment and have fun!
- Save often
- Render tests before final renders

**Need Help?**
- Blender Community: https://blender.community/
- Blender Stack Exchange: https://blender.stackexchange.com/
- Reddit: r/blender

---

*Happy designing! 🏠✨*

*Generated: 2025-11-21*
*Apartment: E.1.5.47*
*Project: Construction Planning*
