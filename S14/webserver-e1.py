import http.server
import socketserver

# Define el puerto
PORT = 8080

# Permite reutilizar el puerto
socketserver.TCPServer.allow_reuse_address = True


# Creamos nuestro handler personalizado
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Si la ruta es la principal "/"
        if self.path == "/":
            contents = "Welcome to my server"
            self.send_response(200)
        else:
            contents = "Resource not available"
            self.send_response(404)

        # Cabeceras
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", len(contents.encode()))
        self.end_headers()

        # Enviar respuesta
        self.wfile.write(contents.encode())


# Usamos nuestro handler
Handler = TestHandler

# Crear y lanzar el servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()