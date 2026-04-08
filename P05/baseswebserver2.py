import http.server
import socketserver
import termcolor
import os

# Define the Server's port
PORT = 8080

# Ruta correcta según el enunciado
PATH = "./P05/html"


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        print("  Command: " + self.command)

        try:
            # Si piden "/" → index.html
            if self.path == "/":
                filepath = PATH + "/index.html"
            else:
                # Construir ruta completa
                filepath = PATH + self.path

            # Normalizar ruta (evita errores con "//")
            filepath = os.path.normpath(filepath)

            # Intentar abrir archivo
            with open(filepath, "r") as page:
                contents = page.read()
                response_code = 200

        except FileNotFoundError:
            # Si no existe → error.html
            with open(PATH + "/error.html", "r") as page:
                contents = page.read()
                response_code = 404

        # Enviar respuesta
        self.send_response(response_code)

        # Tipo de contenido
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

        self.end_headers()

        # Enviar HTML al cliente
        self.wfile.write(contents.encode())

        return


# Evitar error de puerto ocupado
socketserver.TCPServer.allow_reuse_address = True

# Handler
Handler = TestHandler

# Servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()