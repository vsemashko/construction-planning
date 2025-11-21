#!/usr/bin/env python3
"""
Generate SVG 2D floor plan from apartment JSON data
"""
import json
import sys
from pathlib import Path

def load_apartment_data(json_path):
    """Load apartment data from JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_svg_floor_plan(data, output_path):
    """Create SVG floor plan from apartment data"""
    apt = data['apartment']
    dims = apt['dimensions']

    # SVG settings
    scale = 50  # 50 pixels per meter
    margin = 50
    width = int(dims['approximateWidth'] * scale + 2 * margin)
    height = int(dims['approximateDepth'] * scale + 2 * margin)

    svg_lines = []
    svg_lines.append(f'<?xml version="1.0" encoding="UTF-8"?>')
    svg_lines.append(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
    svg_lines.append(f'  <title>Apartment {apt["metadata"]["id"]} - Floor Plan</title>')
    svg_lines.append(f'  <desc>2D Floor plan generated from architectural documents</desc>')

    # Add styles
    svg_lines.append('  <defs>')
    svg_lines.append('    <style>')
    svg_lines.append('      .wall { fill: #333; stroke: #000; stroke-width: 1; }')
    svg_lines.append('      .window { fill: #87CEEB; stroke: #000; stroke-width: 1; }')
    svg_lines.append('      .door { fill: #D2691E; stroke: #000; stroke-width: 1; }')
    svg_lines.append('      .room-label { font-family: Arial, sans-serif; font-size: 12px; fill: #333; text-anchor: middle; }')
    svg_lines.append('      .room-area { font-family: Arial, sans-serif; font-size: 10px; fill: #666; text-anchor: middle; }')
    svg_lines.append('      .floor { fill: #f5f5f5; stroke: #ccc; stroke-width: 1; }')
    svg_lines.append('    </style>')
    svg_lines.append('  </defs>')

    # Background
    svg_lines.append(f'  <rect width="{width}" height="{height}" fill="#fff"/>')

    # Add grid
    svg_lines.append('  <g id="grid" opacity="0.2">')
    for i in range(0, int(dims['approximateWidth']) + 1):
        x = margin + i * scale
        svg_lines.append(f'    <line x1="{x}" y1="{margin}" x2="{x}" y2="{height-margin}" stroke="#ccc" stroke-width="0.5"/>')
    for i in range(0, int(dims['approximateDepth']) + 1):
        y = margin + i * scale
        svg_lines.append(f'    <line x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}" stroke="#ccc" stroke-width="0.5"/>')
    svg_lines.append('  </g>')

    # Draw walls
    svg_lines.append('  <g id="walls">')
    for wall in apt['walls']:
        x1 = margin + wall['start']['x'] * scale
        y1 = margin + wall['start']['y'] * scale
        x2 = margin + wall['end']['x'] * scale
        y2 = margin + wall['end']['y'] * scale
        thickness = wall['thickness'] * scale

        # Determine if wall is horizontal or vertical
        if abs(x2 - x1) > abs(y2 - y1):  # Horizontal wall
            svg_lines.append(f'    <rect x="{min(x1,x2)}" y="{y1-thickness/2}" width="{abs(x2-x1)}" height="{thickness}" class="wall"/>')
        else:  # Vertical wall
            svg_lines.append(f'    <rect x="{x1-thickness/2}" y="{min(y1,y2)}" width="{thickness}" height="{abs(y2-y1)}" class="wall"/>')
    svg_lines.append('  </g>')

    # Add room labels (simplified positions)
    room_positions = {
        "E.1.5.47.1": {"x": 3.25, "y": 11.0},  # Living room
        "E.1.5.47.2": {"x": 3.25, "y": 2.5},   # Room 2
        "E.1.5.47.3": {"x": 1.5, "y": 5.5},    # Room 3
        "E.1.5.47.4": {"x": 1.5, "y": 7.5},    # Room 4
        "E.1.5.47.5": {"x": 5.0, "y": 5.0},    # Bathroom
        "E.1.5.47.6": {"x": 5.0, "y": 3.0},    # WC
        "E.1.5.47.7": {"x": 3.25, "y": 5.5},   # Hall
        "E.1.5.47.8": {"x": 5.0, "y": 7.5},    # Hall 2
    }

    svg_lines.append('  <g id="room-labels">')
    for room in apt['rooms']:
        if room['id'] in room_positions:
            pos = room_positions[room['id']]
            x = margin + pos['x'] * scale
            y = margin + pos['y'] * scale

            svg_lines.append(f'    <text x="{x}" y="{y}" class="room-label">{room["nameEn"]}</text>')
            svg_lines.append(f'    <text x="{x}" y="{y+15}" class="room-area">{room["area"]} m²</text>')
    svg_lines.append('  </g>')

    # Add title and info
    svg_lines.append('  <g id="info">')
    svg_lines.append(f'    <text x="10" y="20" style="font-family: Arial; font-size: 14px; font-weight: bold;">Apartment {apt["metadata"]["id"]}</text>')
    svg_lines.append(f'    <text x="10" y="35" style="font-family: Arial; font-size: 11px;">Total Area: {apt["metadata"]["totalUsableArea"]} m²</text>')
    svg_lines.append(f'    <text x="{width-10}" y="20" style="font-family: Arial; font-size: 10px; text-anchor: end;">Scale: 1:{int(100/scale*100)}cm</text>')
    svg_lines.append('  </g>')

    svg_lines.append('</svg>')

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))

    print(f"✓ SVG floor plan generated: {output_path}")

if __name__ == '__main__':
    # Paths
    base_dir = Path(__file__).parent.parent
    json_path = base_dir / 'output' / 'json' / 'apartment_data.json'
    output_path = base_dir / 'output' / 'svg' / 'floor_plan.svg'

    # Generate SVG
    data = load_apartment_data(json_path)
    create_svg_floor_plan(data, output_path)
