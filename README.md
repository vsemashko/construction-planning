# Construction Planning - Apartment 3D Viewer

Interactive 3D visualization of apartment E.1.5.47 floor plan using Three.js.

## 🚀 Live Demo

The 3D viewer is automatically deployed to GitHub Pages: [View Live Demo](https://vsemashko.github.io/construction-planning/)

## 📁 Project Structure

- `viewer.html` - Main 3D viewer application
- `apartment-data.json` - Apartment geometry and room data
- `docs/` - Floor plan PDFs and documentation
- `3D-MODEL-README.md` - Detailed 3D model documentation

## 🛠️ Local Development

### Option 1: Python Server (Recommended)
```bash
python server.py
```
Then open http://localhost:8000

### Option 2: Any HTTP Server
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx http-server -p 8000
```

## 🚀 Deployment

The project uses GitHub Actions for automatic deployment to GitHub Pages.

### How it works:
1. Push changes to `main` or the current feature branch
2. GitHub Actions automatically builds and deploys
3. View the updated site at the GitHub Pages URL

### Manual Deployment Trigger:
Go to Actions tab → "Deploy to GitHub Pages" → "Run workflow"

## 📐 Modifying the 3D Model

Edit `apartment-data.json` to update:
- Room dimensions and positions
- Wall configurations
- Room colors and materials
- Room metadata (names, areas)

After pushing changes, the site will automatically redeploy with your updates.

## 🏗️ Features

- Interactive 3D apartment visualization
- Room labels with area information
- Orbit controls for navigation
- Responsive design
- Automatic deployment pipeline

## 📋 Room Layout

| Room | Area (m²) |
|------|-----------|
| Living Room / Salon | 27.64 |
| Bedroom 1 | 10.48 |
| Bedroom 2 | 7.85 |
| Bedroom 3 | 7.24 |
| Bathroom 1 | 5.42 |
| Corridor / Hall | 6.51 |
| Hall / Kitchen | 8.47 |
| Lavatory / WC | 1.82 |
| Balcony | 9.99 |

**Total Area:** ~85.42 m²
