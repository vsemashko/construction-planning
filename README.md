# Construction Planning - Apartment E.1.5.47

Convert architectural PDF documents into multiple 3D formats for interior design, visualization, and planning.

**Apartment:** E.1.5.47 | **Floor:** 5 | **Area:** 73.97 m² | **Rooms:** 8 + Balcony

---

## 🎯 What This Project Does

Converts architectural PDF documents into **4 different formats** that you can use for:
- 📐 **Interior Design** (Blender, SketchUp)
- 🌐 **Web Visualization** (Three.js, WebGL)
- 📊 **Data Processing** (JSON, databases)
- 📄 **Documentation** (SVG, presentations)

---

## 🚀 Quick Start

### 1️⃣ View the Apartment

**Fastest way to see everything:**
```bash
# Open the interactive viewer
open output/html/viewer.html
```

Displays all formats side-by-side with interactive 3D viewer.

### 2️⃣ Import to Blender (Recommended for Design)

**5-minute setup:**

1. Open Blender
2. Scripting workspace → Open `scripts/blender_import.py`
3. Update `BASE_PATH` to your project folder
4. Press `Alt+P` to run

✅ Automatically sets up materials, lighting, cameras!

**See:** [BLENDER_QUICKSTART.md](BLENDER_QUICKSTART.md) for step-by-step guide

### 3️⃣ Explore the Formats

All generated files are in `output/`:

```
output/
├── json/apartment_data.json    # All data and measurements
├── svg/floor_plan.svg          # 2D floor plan (scalable)
├── obj/apartment.obj           # 3D model for CAD software
├── gltf/apartment.gltf         # 3D model for web/AR/VR
└── html/viewer.html            # Interactive comparison
```

---

## 📁 Project Structure

```
construction-planning/
│
├── docs/                           # Original PDF documents
│   ├── E.1.5.47_2.pdf             # Floor plan
│   ├── E.1.5.47_ARCH_2024.05.10.pdf   # Architecture
│   ├── E.1.5.47_CO_2024.05.10.pdf     # Heating
│   └── E.1.5.47_ELE_2024.05.10.pdf    # Electrical
│
├── output/                         # Generated formats
│   ├── json/                       # Structured data
│   ├── svg/                        # 2D vector graphics
│   ├── obj/                        # 3D CAD format
│   ├── gltf/                       # 3D web format
│   └── html/                       # Interactive viewer
│
├── scripts/                        # Generation scripts
│   ├── generate_json.py           # (embedded in others)
│   ├── generate_svg.py            # Create SVG floor plan
│   ├── generate_obj.py            # Create OBJ 3D model
│   ├── generate_gltf.py           # Create glTF 3D model
│   └── blender_import.py          # Blender automation script
│
└── docs/                          # Documentation
    ├── README.md                  # This file
    ├── PLAN_3D_CONVERSION.md     # Initial planning document
    ├── FORMAT_COMPARISON.md       # Detailed format comparison
    ├── BLENDER_QUICKSTART.md     # 5-minute Blender guide
    └── BLENDER_GUIDE.md          # Complete Blender tutorial
```

---

## 📊 Available Formats

### 1. JSON - Structured Data (7.0 KB)
**What it is:** Complete apartment data in machine-readable format

**Contains:**
- Room dimensions and areas
- Window/door specifications
- Heating system (6 radiators)
- Electrical layout
- Complete metadata

**Use for:**
- Data processing and analysis
- Integration with other software
- Database import
- Custom applications

**Open with:** Any text editor, programming tools

---

### 2. SVG - 2D Floor Plan (4.2 KB)
**What it is:** Scalable vector graphics floor plan

**Features:**
- Wall layouts with grid
- Room labels and areas
- Infinitely scalable
- Print-ready

**Use for:**
- Documentation and presentations
- Web display
- Print materials
- Real estate listings

**Open with:** Web browsers, Inkscape, Adobe Illustrator

---

### 3. OBJ - Universal 3D Model (1.7 KB + materials)
**What it is:** Industry-standard 3D format

**Specs:**
- 48 vertices, 36 faces
- Includes material definitions (.mtl)
- Metric scale (1 unit = 1 meter)

**Use for:**
- Import to Blender, SketchUp, 3ds Max
- CAD software
- Further 3D modeling
- Interior design

**Open with:** Blender, SketchUp, AutoCAD, MeshLab

---

### 4. glTF - Modern 3D Web Format (2.9 KB)
**What it is:** Web-optimized 3D format

**Specs:**
- 48 vertices, 72 triangles
- PBR materials (Physically Based Rendering)
- Base64-encoded buffers

**Use for:**
- Web-based 3D viewers
- Mobile applications
- AR/VR experiences
- Three.js, Babylon.js

**Open with:** Web browsers (Three.js), Blender

---

## 🎨 Use Cases

### Interior Design
**Best Format:** OBJ or glTF + Blender
```
1. Import using blender_import.py script
2. Add furniture and decorations
3. Customize materials and colors
4. Render photorealistic images
```
**See:** [BLENDER_GUIDE.md](BLENDER_GUIDE.md)

### Web Visualization
**Best Format:** glTF
```javascript
// Use with Three.js
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const loader = new GLTFLoader();
loader.load('output/gltf/apartment.gltf', (gltf) => {
  scene.add(gltf.scene);
});
```

### Documentation & Presentations
**Best Format:** SVG
- Open in web browser
- Insert in PowerPoint/Keynote
- Print at any size
- Edit in Inkscape/Illustrator

### Data Analysis
**Best Format:** JSON
```python
import json
with open('output/json/apartment_data.json') as f:
    data = json.load(f)
    total_area = data['apartment']['metadata']['totalUsableArea']
```

---

## 🛠️ Regenerating Formats

All formats are generated from the PDF documents using Python scripts.

```bash
# From project root
cd construction-planning

# Generate all formats
python3 scripts/generate_svg.py
python3 scripts/generate_obj.py
python3 scripts/generate_gltf.py
```

**Requirements:**
- Python 3.7+
- No additional dependencies needed!

---

## 📚 Documentation

| Document | Description | When to Use |
|----------|-------------|-------------|
| **README.md** | This file - project overview | Start here |
| **BLENDER_QUICKSTART.md** | 5-minute Blender setup | Want to design NOW |
| **BLENDER_GUIDE.md** | Complete Blender tutorial | Learn interior design |
| **FORMAT_COMPARISON.md** | Detailed format analysis | Choose best format |
| **PLAN_3D_CONVERSION.md** | Original planning document | Technical details |
| **output/README.md** | Output files guide | Working with exports |

---

## 🎓 Learning Resources

### Blender (Interior Design)
- **Quick Start:** [BLENDER_QUICKSTART.md](BLENDER_QUICKSTART.md) - 5 minutes
- **Full Guide:** [BLENDER_GUIDE.md](BLENDER_GUIDE.md) - Complete tutorial
- **YouTube:** Blender Guru, Grant Abbitt (search "interior design")

### Three.js (Web 3D)
- View source of `output/html/viewer.html` for example
- Official docs: https://threejs.org/docs/
- Three.js Journey: https://threejs-journey.com/

### Format Details
- [FORMAT_COMPARISON.md](FORMAT_COMPARISON.md) - 15+ pages comparing formats

---

## 🏗️ Apartment Specifications

### Basic Info
- **ID:** E.1.5.47
- **Building:** SOHO 12
- **Floor:** 5 (Piętro)
- **Total Usable Area:** 73.97 m²
- **Ceiling Height:** 2.60 m
- **Balcony:** 9.99 m²

### Rooms
| # | Room | Area (m²) |
|---|------|-----------|
| 1 | Living Room + Kitchenette | 27.44 |
| 2 | Room | 10.48 |
| 3 | Room | 7.95 |
| 4 | Room | 7.94 |
| 5 | Bathroom | 5.42 |
| 6 | WC | 1.62 |
| 7 | Hall | 6.61 |
| 8 | Hall | 4.47 |
| 9 | Balcony | 9.99 |

### Systems
- **Heating:** Central heating, 6 radiators (total 3080W)
- **Electrical:** 230V outlets, 400V for electric stove
- **Communication:** Video intercom, RJ45, TV/SAT
- **Ventilation:** Mechanical with wall vents

### Developer & Architect
- **Developer:** Yawa Sp. z o.o. 4 Sp. k.
- **Architect:** HRA Architekci Sp. z o.o. Sp.k
- **Location:** ul. Mińska / ul. Żupnicza, Warsaw
- **Date:** May 10, 2024

---

## 🎯 Recommended Workflows

### Workflow 1: Quick Visualization
**Time:** 5 minutes
```
1. Open output/html/viewer.html
2. View all formats side-by-side
3. Download needed format
```

### Workflow 2: Interior Design
**Time:** 1-2 hours
```
1. Open Blender
2. Run scripts/blender_import.py
3. Add furniture from libraries
4. Customize materials
5. Render beautiful images
```

### Workflow 3: Web Application
**Time:** 2-4 hours
```
1. Copy output/gltf/apartment.gltf to your project
2. Set up Three.js scene (use viewer.html as reference)
3. Add interactivity (room selection, etc.)
4. Deploy to web
```

### Workflow 4: Data Analysis
**Time:** 30 minutes
```
1. Load output/json/apartment_data.json
2. Process data with Python/JavaScript
3. Generate reports, calculations, etc.
```

---

## 🤝 Contributing

This is a project template for converting architectural documents to 3D formats.

**Potential improvements:**
- More detailed geometry (interior walls, doors, windows)
- Furniture placement from floor plans
- Automated PDF parsing
- More export formats (IFC, DXF, USDZ)
- Enhanced materials and textures

---

## 📜 License

Generated from architectural documents provided by:
- **Developer:** Yawa Sp. z o.o. 4 Sp. k.
- **Architect:** HRA Architekci Sp. z o.o. Sp.k

Please respect the original intellectual property rights.

---

## 🆘 Need Help?

### Common Questions

**Q: Which format should I use?**
A: See [FORMAT_COMPARISON.md](FORMAT_COMPARISON.md) for detailed comparison.
- Interior design → OBJ + Blender
- Web app → glTF
- Documentation → SVG
- Data processing → JSON

**Q: How do I import to Blender?**
A: See [BLENDER_QUICKSTART.md](BLENDER_QUICKSTART.md) - takes 5 minutes!

**Q: Can I edit the 3D models?**
A: Yes! Both OBJ and glTF can be edited in Blender and other 3D software.

**Q: How do I add furniture?**
A: Import the apartment to Blender, then add furniture from asset libraries.
See [BLENDER_GUIDE.md](BLENDER_GUIDE.md) section "Interior Design Workflow".

**Q: Can I use this for other apartments?**
A: Yes! Modify the Python scripts to extract data from your PDF documents.

### Support Resources
- **Blender:** https://blender.stackexchange.com/
- **Three.js:** https://discourse.threejs.org/
- **General 3D:** r/3Dmodeling, r/blender on Reddit

---

## ✨ What's Next?

1. ✅ PDF documents imported
2. ✅ Multiple formats generated
3. ✅ Blender import ready
4. 🎨 **Your turn!** Design your dream apartment

**Start here:**
- **New to 3D?** → [BLENDER_QUICKSTART.md](BLENDER_QUICKSTART.md)
- **Want to learn?** → [BLENDER_GUIDE.md](BLENDER_GUIDE.md)
- **Just browsing?** → Open `output/html/viewer.html`

---

**Happy designing! 🏠✨**

*Last updated: 2025-11-21*
*Project: Architectural Document to 3D Conversion*
