# Blender Quick Start - 5 Minutes Setup

Get your apartment 3D model into Blender in 5 minutes or less!

---

## 🚀 Fastest Method - Automated Script

### Step 1: Download & Install Blender
- Visit: https://www.blender.org/download/
- Download and install (it's free!)
- Requires: Blender 2.8 or newer

### Step 2: Open the Import Script
1. Launch Blender
2. Click "Scripting" tab at top
3. Click "Open" button
4. Navigate to: `construction-planning/scripts/blender_import.py`

### Step 3: Update Path
Find this line:
```python
BASE_PATH = "/home/user/construction-planning"
```

Change to YOUR path:
- **Windows:** `BASE_PATH = "C:/Users/YourName/construction-planning"`
- **Mac:** `BASE_PATH = "/Users/YourName/construction-planning"`
- **Linux:** `BASE_PATH = "/home/yourname/construction-planning"`

### Step 4: Run!
- Press `Alt+P` OR
- Click the ▶ "Run Script" button

### Step 5: Enjoy!
Your apartment is now loaded with:
- ✅ Walls, floors, ceiling
- ✅ Professional materials
- ✅ 3 camera angles
- ✅ Beautiful lighting
- ✅ Ready to render!

---

## 📸 Quick Camera Views

Switch between views:
- Press `Numpad 0` - Camera view
- Press `Numpad 7` - Top-down view
- Press `Numpad 1` - Front view
- Drag `Middle Mouse` - Orbit around

Select camera:
- `Camera_Overview` - Best for presentation
- `Camera_TopDown` - Floor plan view
- `Camera_Interior` - Inside the apartment

---

## 🎨 Essential Controls

| What You Want | Press This |
|--------------|-----------|
| Move camera around | Middle Mouse Button + Drag |
| Zoom in/out | Scroll Wheel |
| Select object | Left Click |
| Move object | `G` (grab) |
| Rotate object | `R` |
| Scale object | `S` |
| Delete | `X` |
| Undo | `Ctrl+Z` |
| Save | `Ctrl+S` |

---

## 🖼️ Render Your First Image

**Quick Render:**
1. Press `Numpad 0` (camera view)
2. Press `F12` (render)
3. Wait 10-30 seconds
4. Image → Save As → Choose location
5. Done!

**Better Quality:**
1. Click "Render Properties" tab (camera icon on right)
2. Change "Render Engine" to "Cycles"
3. Press `F12`
4. Wait 1-3 minutes
5. Save!

---

## 🪑 Add Furniture (Simple)

**Add a basic object:**
1. `Shift+A` → Mesh → Cube (or other shape)
2. `G` to move it
3. `S` to scale it
4. `R` to rotate it

**Change color:**
1. Click "Shading" workspace at top
2. Select your object
3. Find "Base Color" in bottom panel
4. Click the color box → Choose color

---

## 🎯 If Something Goes Wrong

**Model looks too small:**
- Select all: `A`
- Scale up: `S` → `10` → `Enter`

**Scene is too dark:**
- Add light: `Shift+A` → Light → Sun
- Increase power: Light Properties → Power → 5.0

**Can't see anything:**
- Press `Numpad .` (period) - Frame all objects
- Or: View → Frame All

**Script error "path not found":**
- Check BASE_PATH matches your actual folder
- Use forward slashes: `C:/` not `C:\`

---

## 📚 Want to Learn More?

See **BLENDER_GUIDE.md** for:
- Complete tutorial
- Interior design workflow
- Advanced rendering
- Material editing
- Troubleshooting
- Learning resources

---

## 💾 Manual Import (Alternative)

If you prefer not to use the script:

**Import OBJ:**
1. File → Import → Wavefront (.obj)
2. Navigate to: `output/obj/apartment.obj`
3. Click "Import OBJ"

**Import glTF:**
1. File → Import → glTF 2.0
2. Navigate to: `output/gltf/apartment.gltf`
3. Click "Import glTF 2.0"

---

## 🎓 Next Steps

1. ✅ Import apartment (done!)
2. 🪑 Add furniture
3. 🎨 Customize colors/materials
4. 💡 Adjust lighting
5. 📸 Render beautiful images
6. 🏠 Share your design!

---

**That's it! You're ready to design!** 🎉

For detailed tutorials, see:
- **BLENDER_GUIDE.md** - Complete guide
- **FORMAT_COMPARISON.md** - File format details
- **PLAN_3D_CONVERSION.md** - Project overview

**Free Learning Resources:**
- Blender Guru on YouTube (excellent beginner tutorials)
- Official Blender Manual: https://docs.blender.org
- r/blender subreddit for community help

---

*Quick Start Guide - Apartment E.1.5.47*
*Get designing in 5 minutes! ⚡*
