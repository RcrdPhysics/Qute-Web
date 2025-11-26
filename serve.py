#!/usr/bin/env python3
"""Simple static server with bind option.

Usage:
  python3 serve.py --bind 127.0.0.1 --port 8000

This is a tiny wrapper around http.server that accepts a --bind argument
(similar to Python 3.8+ http.server) and serves the current directory.
"""
import argparse
import http.server
import socketserver
import sys

parser = argparse.ArgumentParser(description="Serve the current directory over HTTP")
parser.add_argument("--bind", default="127.0.0.1", help="IP address to bind to (default: 127.0.0.1)")
parser.add_argument("--port", type=int, default=8000, help="Port to serve on (default: 8000)")
args = parser.parse_args()

class _Handler(http.server.SimpleHTTPRequestHandler):
    pass

try:
    with socketserver.TCPServer((args.bind, args.port), _Handler) as httpd:
        sa = httpd.socket.getsockname()
        print(f"Serving HTTP on {sa[0]} port {sa[1]} (http://{sa[0]}:{sa[1]}/) ...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            httpd.server_close()
except OSError as e:
    print(f"Error: {e}")
    sys.exit(1)
