import http.server
import socketserver
import webbrowser
import threading
import sys

def find_free_port(start_port=8000):
    port = start_port
    for p in range(port, port + 100):
        try:
            with socketserver.TCPServer(("", p), None) as s:
                return p
        except OSError:
            continue
    return port

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        mimetype = super().guess_type(path)
        if path.endswith('.md'):
            return 'text/markdown; charset=utf-8'
        if mimetype and mimetype.startswith('text/') and 'charset=' not in mimetype:
            return mimetype + '; charset=utf-8'
        return mimetype

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def start_server_in_thread(port):
    handler = NoCacheHandler
    httpd = socketserver.TCPServer(("", port), handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    return thread, httpd

def main():
    port = find_free_port(8000)
    url = f"http://localhost:{port}/visualize.html"
    print("=" * 60)
    print(f"  Wiki Cognitive Graph Visualizer")
    print(f"  Running local server at: {url}")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 60)
    webbrowser.open(url)
    
    handler = NoCacheHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped cleanly.")
            sys.exit(0)

if __name__ == '__main__':
    main()
