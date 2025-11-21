# Apartment 3D Model Viewer

This project converts apartment floor plans into interactive 3D models that can be viewed in a web browser.

## Files

- `apartment-data.json` - Contains the 3D geometry data for apartment E.1.5.47
- `viewer.html` - Interactive 3D viewer powered by Three.js
- `docs/` - Original architectural plans (PDF format)

## Apartment E.1.5.47 Details

- **Floor**: 5
- **Total Area**: 79.32 m²
- **Ceiling Height**: 2.8 m
- **Rooms**: 9 rooms including living room, bedrooms, kitchen, bathrooms, and balcony

## Features

### 3D Viewer Capabilities

1. **Interactive Navigation**
   - Rotate: Left mouse button + drag
   - Zoom: Mouse wheel
   - Pan: Right mouse button + drag

2. **Room Visualization**
   - Color-coded rooms by type
   - Room labels with area information
   - Click on rooms in the sidebar to focus on them

3. **View Controls**
   - Reset View: Return to default camera position
   - Toggle View: Switch between perspective and top-down views
   - Show/Hide: Walls, labels, and fixtures

4. **Room Types & Colors**
   - Living Room: Blue
   - Bedrooms: Green
   - Kitchen: Orange
   - Bathroom: Cyan
   - Corridors: Light Green
   - Balcony: Purple

## How to Use

### Option 1: Simple Python Server (Recommended)

1. Run the included server script:
```bash
python3 server.py
```

2. Open your browser to: `http://localhost:8000/viewer.html`

### Option 2: Manual Server Setup

1. Start a local web server in this directory:
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (if you have http-server installed)
npx http-server -p 8000
```

2. Open your browser to: `http://localhost:8000/viewer.html`

### Option 3: VS Code Live Server

1. Install the "Live Server" extension in VS Code
2. Right-click on `viewer.html` and select "Open with Live Server"

## Customizing the Model

### Modifying Room Geometry

Edit `apartment-data.json` to adjust:
- Room vertices (coordinates in meters)
- Wall positions and thickness
- Door and window locations
- Fixture positions

### Adding More Apartments

1. Create a new JSON file following the same structure as `apartment-data.json`
2. Update the `fetch('apartment-data.json')` line in `viewer.html` to load your new file
3. Or create a dropdown selector to switch between multiple apartments

## Technical Details

### Technologies Used

- **Three.js** (v0.160.0) - 3D rendering library
- **OrbitControls** - Camera navigation
- **CSS2DRenderer** - Room labels overlay
- **ES6 Modules** - Modern JavaScript structure

### Browser Compatibility

Works in all modern browsers that support:
- WebGL
- ES6 Modules
- CSS3

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Future Enhancements

Potential improvements for the 3D model:

1. **Furniture Placement**
   - Add 3D furniture models
   - Drag-and-drop furniture positioning
   - Save/load furniture layouts

2. **Material Selection**
   - Different floor materials (wood, tile, carpet)
   - Wall colors and textures
   - Window treatments

3. **Measurements**
   - Interactive measurement tool
   - Distance calculator
   - Area calculator

4. **Lighting Simulation**
   - Natural light simulation
   - Time-of-day lighting
   - Custom light fixtures

5. **Export Options**
   - Export to glTF/GLB format
   - Generate printable floor plans
   - Create walkthrough animations

6. **VR/AR Support**
   - WebXR integration
   - Virtual reality walkthrough
   - Augmented reality preview

## Troubleshooting

### Blank Screen
- Ensure you're running a local server (CORS restrictions prevent loading from `file://`)
- Check browser console for errors
- Verify `apartment-data.json` is in the same directory as `viewer.html`

### Labels Not Showing
- Click the "Show Labels" checkbox in the controls panel
- Labels may be hidden behind walls - try rotating the view

### Performance Issues
- Try reducing the number of rooms or simplifying geometry
- Disable shadows in the code if needed
- Use a modern browser with good WebGL support

## License

This 3D viewer is provided as-is for visualization and planning purposes.

## Contact

For questions or improvements, please create an issue in the repository.
