# Generated Formats - Apartment E.1.5.47

This directory contains multiple format outputs generated from the architectural PDF documents of apartment E.1.5.47.

## Directory Structure

```
output/
├── json/
│   └── apartment_data.json        # Structured data with all measurements
├── svg/
│   └── floor_plan.svg             # 2D vector floor plan
├── obj/
│   ├── apartment.obj              # 3D model geometry
│   └── apartment.mtl              # Material definitions
├── gltf/
│   └── apartment.gltf             # Modern 3D web format
└── html/
    └── viewer.html                # Interactive viewer for all formats
```

## Quick Start

### View All Formats
Open `html/viewer.html` in a web browser to see an interactive comparison of all formats.

### Individual Formats

#### JSON Data
```bash
# View in terminal
cat json/apartment_data.json

# Or open in any text editor
code json/apartment_data.json
```

#### SVG Floor Plan
```bash
# Open in browser
open svg/floor_plan.svg

# Or edit in Inkscape
inkscape svg/floor_plan.svg
```

#### OBJ 3D Model
```bash
# Open in Blender (if installed)
blender obj/apartment.obj

# Or use MeshLab
meshlab obj/apartment.obj
```

#### glTF 3D Model
```bash
# View in browser with Three.js viewer
# Or import into Blender
blender gltf/apartment.gltf
```

## Format Details

### JSON (Data)
- **Size:** ~5 KB
- **Use:** Data processing, integration, analysis
- **Open with:** Any text editor, programming tools

### SVG (2D Vector)
- **Size:** ~8 KB
- **Use:** Documentation, web display, printing
- **Open with:** Web browsers, Inkscape, Adobe Illustrator

### OBJ (3D Universal)
- **Size:** ~3 KB (+ materials)
- **Use:** CAD software, 3D modeling, architecture
- **Open with:** Blender, SketchUp, 3ds Max, AutoCAD

### glTF (3D Web)
- **Size:** ~15 KB
- **Use:** Web applications, AR/VR, mobile apps
- **Open with:** Web browsers (Three.js), Blender

## Use Cases by Format

| Need | Recommended Format |
|------|-------------------|
| Print floor plan | SVG |
| Design in SketchUp | OBJ |
| Build web viewer | glTF |
| Process data | JSON |
| Documentation | SVG |
| Further modeling | OBJ |
| AR experience | glTF |
| Data analysis | JSON |

## Regenerating Formats

To regenerate any format, run the corresponding script:

```bash
# From project root directory
cd construction-planning

# Generate all formats
python3 scripts/generate_svg.py
python3 scripts/generate_obj.py
python3 scripts/generate_gltf.py
```

## More Information

See `FORMAT_COMPARISON.md` in the project root for a detailed comparison of all formats, including:
- Technical specifications
- Advantages and disadvantages
- Software compatibility
- Conversion options
- Recommendations by use case

## Source Data

All formats are generated from:
- `docs/E.1.5.47_2.pdf` - Floor plan
- `docs/E.1.5.47_ARCH_2024.05.10.pdf` - Architectural details
- `docs/E.1.5.47_CO_2024.05.10.pdf` - Heating system
- `docs/E.1.5.47_ELE_2024.05.10.pdf` - Electrical installation

## License

Generated from architectural documents provided by:
- Developer: Yawa Sp. z o.o. 4 Sp. k.
- Architect: HRA Architekci Sp. z o.o. Sp.k

Please respect the original intellectual property rights.
