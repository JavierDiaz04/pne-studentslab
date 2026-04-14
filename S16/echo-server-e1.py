import http.server
import socketserver
import urllib.parse

PORT = 8080

class EchoHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if path == "/":
            # Servir formulario
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("S16/html/form-e1.html", "r") as f:
                self.wfile.write(f.read().encode())

        elif path == "/echo":
            # Obtener mensaje
            query = urllib.parse.parse_qs(parsed_path.query)
            message = query.get("message", [""])[0]

            # Respuesta dinámica
            response_html = f"""
            <html>
            <head><title>Echo</title></head>
            <body>
                <h1>Echo message</h1>
                <p>{message}</p>
                <a href="/">Back</a>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response_html.encode())

        else:
            # Error
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("S16/html/error.html", "r") as f:
                self.wfile.write(f.read().encode())


# Ejecutar servidor
with socketserver.TCPServer(("", PORT), EchoHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()