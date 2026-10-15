"""Servidor multi-hilo para el visor del almanaque.

python -m http.server es mono-hilo: atiende una peticion a la vez y el visor
pide muchas imagenes simultaneas, asi que algunas cargas se abortan y las
texturas salen negras. Este sirve cada peticion en su propio hilo.

Uso:  python servir.py 8080
"""
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # sin cache: si regeneras las paginas, el navegador no sirve las viejas
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
print(f"visor en http://localhost:{port}   (Ctrl+C para parar)")
try:
    srv.serve_forever()
except KeyboardInterrupt:
    pass
