#!/usr/bin/env python3
"""
Proxy HTTP server to serve static files and forward API requests to backend.
Configured for Replit environment on port 5000.
"""
import http.server
import socketserver
import urllib.request
import urllib.error
import json

PORT = 5000
HOST = "0.0.0.0"
FRONTEND_DIR = "frontend"
BACKEND_URL = "http://127.0.0.1:8000"

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler with API proxy and cache control"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)
    
    def do_GET(self):
        if self.path.startswith('/api/'):
            self.proxy_request()
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path.startswith('/api/'):
            self.proxy_request()
        else:
            self.send_error(405, "Method Not Allowed")
    
    def do_PUT(self):
        if self.path.startswith('/api/'):
            self.proxy_request()
        else:
            self.send_error(405, "Method Not Allowed")
    
    def do_DELETE(self):
        if self.path.startswith('/api/'):
            self.proxy_request()
        else:
            self.send_error(405, "Method Not Allowed")
    
    def do_OPTIONS(self):
        if self.path.startswith('/api/'):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
        else:
            super().do_OPTIONS()
    
    def proxy_request(self):
        """Forward API requests to backend server"""
        # Remove /api prefix
        backend_path = self.path.replace('/api', '', 1)
        backend_url = f"{BACKEND_URL}{backend_path}"
        
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length) if content_length > 0 else None
            
            # Prepare request
            headers = {'Content-Type': 'application/json'}
            req = urllib.request.Request(
                backend_url,
                data=body,
                headers=headers,
                method=self.command
            )
            
            # Forward to backend
            with urllib.request.urlopen(req, timeout=30) as response:
                self.send_response(response.status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(response.read())
                
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(e.read())
            
        except urllib.error.URLError as e:
            self.send_response(503)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error = json.dumps({"error": f"Backend unavailable: {str(e)}"})
            self.wfile.write(error.encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error = json.dumps({"error": f"Proxy error: {str(e)}"})
            self.wfile.write(error.encode())
    
    def end_headers(self):
        # Disable caching for static files
        if not self.path.startswith('/api/'):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), ProxyHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"Frontend server running at http://{HOST}:{PORT}/")
        print(f"Serving static files from {FRONTEND_DIR}/ directory")
        print(f"Proxying /api/* requests to {BACKEND_URL}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
