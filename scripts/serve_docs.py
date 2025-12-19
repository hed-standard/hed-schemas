#!/usr/bin/env python3
"""
Cross-platform script to serve HED documentation locally using Python's HTTP server.

This script:
1. Checks that documentation has been built
2. Starts a local HTTP server on port 8000
3. Provides instructions for viewing the documentation

Usage:
    python scripts/serve_docs.py [--port PORT]

Options:
    --port PORT    Port to serve on (default: 8000)
"""

import argparse
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path


def main():
    """Serve the built Sphinx documentation locally."""
    parser = argparse.ArgumentParser(description="Serve HED documentation locally")
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to serve on (default: 8000)"
    )
    parser.add_argument(
        "--no-browser", action="store_true", help="Don't automatically open browser"
    )
    args = parser.parse_args()

    # Get the repository root and build directory
    repo_root = Path(__file__).parent.parent
    html_dir = repo_root / "docs" / "_build" / "html"

    # Check if documentation has been built
    if not html_dir.exists() or not (html_dir / "index.html").exists():
        print("❌ Error: Documentation has not been built yet.", file=sys.stderr)
        print(
            f"\nThe directory {html_dir} does not exist or is empty.", file=sys.stderr
        )
        print("\nPlease build the documentation first:")
        print("    python scripts/build_docs.py")
        print()
        return 1

    print("=" * 70)
    print("HED schemas documentation server")
    print("=" * 70)
    print(f"\n📁 Serving from: {html_dir}")
    print(f"🌐 Open your browser to: http://localhost:{args.port}")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 70)
    print()

    # Optionally open browser
    if not args.no_browser:
        try:
            webbrowser.open(f"http://localhost:{args.port}")
        except Exception:
            pass  # Silently fail if browser can't be opened

    # Change to the HTML directory and start server
    try:
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", args.port), Handler) as httpd:
            # Change directory for the handler
            import os

            os.chdir(html_dir)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped.")
        return 0
    except OSError as e:
        if "address already in use" in str(e).lower():
            print(f"\n❌ Error: Port {args.port} is already in use.", file=sys.stderr)
            print("\nTry a different port:")
            print(f"    python scripts/serve_docs.py --port {args.port + 1}")
        else:
            print(f"\n❌ Error starting server: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
