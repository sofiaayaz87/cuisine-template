#!/usr/bin/env python3
"""
Simple HTTP server to serve static files for the Cuisine restaurant template.
Configured for Replit environment on port 5000.
"""
import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class CacheControlHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to disable caching for Replit iframe preview"""
    
    def end_headers(self):
        # Disable caching to ensure updates are visible in Replit's iframe
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer((HOST, PORT), CacheControlHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"Server running at http://{HOST}:{PORT}/")
        print("Serving static files from current directory")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
