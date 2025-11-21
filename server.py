#!/usr/bin/env python3
"""
Simple HTTP server for the Apartment 3D Viewer
This script starts a local web server to view the 3D apartment model.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow loading of modules
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        sys.stdout.write(f"\033[92m[Server]\033[0m {format % args}\n")

def main():
    # Change to the script directory
    os.chdir(Path(__file__).parent)

    # Create server
    handler = MyHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            url = f"http://localhost:{PORT}/viewer.html"

            print("\n" + "="*60)
            print(f"\033[94m🏢 Apartment 3D Viewer Server\033[0m")
            print("="*60)
            print(f"\n\033[92m✓ Server running on port {PORT}\033[0m")
            print(f"\n\033[96m🌐 Open your browser to:\033[0m")
            print(f"   {url}")
            print(f"\n\033[93m💡 Tips:\033[0m")
            print("   - Use mouse to rotate, zoom, and pan")
            print("   - Click rooms in the sidebar to focus on them")
            print("   - Use the control panel to toggle views")
            print(f"\n\033[91m⏹  Press Ctrl+C to stop the server\033[0m")
            print("="*60 + "\n")

            # Try to open browser automatically
            try:
                webbrowser.open(url)
                print("\033[92m✓ Browser opened automatically\033[0m\n")
            except:
                print("\033[93m⚠ Could not open browser automatically\033[0m")
                print(f"  Please open {url} manually\n")

            # Start serving
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\n\033[91m⏹  Server stopped\033[0m")
        print("\033[92m✓ Thank you for using Apartment 3D Viewer!\033[0m\n")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Address already in use
            print(f"\n\033[91m✗ Error: Port {PORT} is already in use\033[0m")
            print(f"  Try closing other applications or use a different port\n")
        else:
            print(f"\n\033[91m✗ Error: {e}\033[0m\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
