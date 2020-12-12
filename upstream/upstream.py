#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn, TCPServer


class StaticHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hooray, it works!\n\n")
        self.wfile.write(
            b"If you're seeing this, you have successfully authorized through Envoy's OAuth2 filter!\n\n"
        )
        self.wfile.write(f"GET {self.path}\n".encode())
        for k, v in self.headers.items():
            self.wfile.write(f"{k}: {v}\n".encode())


class ReuseAddrTCPServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True


def serve(host: str, port: int) -> None:
    with ReuseAddrTCPServer((host, port), StaticHandler) as httpd:
        print(f"Serving at {host}:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--listen-host", "-l", type=str, default="", required=False)
    parser.add_argument("--listen-port", "-p", type=int, default=8000, required=False)
    args = parser.parse_args()

    serve(args.listen_host, args.listen_port)
