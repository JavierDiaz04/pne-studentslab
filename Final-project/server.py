from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import urllib.request
import json

PORT = 8080


def call_ensembl(url):
    """Simple helper to call Ensembl API without external libraries"""
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except:
        return None


def error_html(msg):
    return f"""
    <html>
    <body style="font-family:Arial">
        <h2 style="color:red;">Error</h2>
        <p>{msg}</p>
        <a href="/">Go back</a>
    </body>
    </html>
    """


MAIN_PAGE = """
<html>
<head>
    <title>Genome Browser</title>
</head>
<body style="font-family:Arial">

<h1>Genome Browser</h1>

<h3>List species</h3>
<form action="/listSpecies">
    Limit: <input name="limit" type="number">
    <input type="submit" value="Send">
</form>

<h3>Karyotype</h3>
<form action="/karyotype">
    Species: <input name="species" type="text">
    <input type="submit" value="Send">
</form>

<h3>Chromosome length</h3>
<form action="/chromosomeLength">
    Species: <input name="species" type="text">
    Chromosome: <input name="chromo" type="text">
    <input type="submit" value="Send">
</form>

</body>
</html>
"""


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        url_parts = urlparse(self.path)
        path = url_parts.path
        args = parse_qs(url_parts.query)

        # HOME
        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(MAIN_PAGE.encode())
            return

        # LIST SPECIES
        if path == "/listSpecies":

            data = call_ensembl("https://rest.ensembl.org/info/species?content-type=application/json")

            if not data:
                html = error_html("Cannot get species data")
            else:
                species = data.get("species", [])

                limit = args.get("limit", [None])[0]
                if limit:
                    try:
                        limit = int(limit)
                    except:
                        limit = None

                html = "<h1>Species</h1><ul>"

                count = 0
                for s in species:
                    html += f"<li>{s['display_name']}</li>"
                    count += 1
                    if limit and count >= limit:
                        break

                html += "</ul><a href='/'>Back</a>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        # KARYOTYPE
        if path == "/karyotype":

            species = args.get("species", [None])[0]

            if not species:
                html = error_html("Missing species")
            else:

                url = f"https://rest.ensembl.org/info/assembly/{species}?content-type=application/json"
                data = call_ensembl(url)

                if not data:
                    html = error_html("Species not found or API error")
                else:
                    karyotype = data.get("karyotype", [])

                    html = f"<h1>Karyotype: {species}</h1><ul>"

                    for c in karyotype:
                        html += f"<li>{c}</li>"

                    html += "</ul><a href='/'>Back</a>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        # CHROMOSOME LENGTH
        if path == "/chromosomeLength":

            species = args.get("species", [None])[0]
            chromo = args.get("chromo", [None])[0]

            if not species or not chromo:
                html = error_html("Missing parameters")
            else:

                url = f"https://rest.ensembl.org/info/assembly/{species}?content-type=application/json"
                data = call_ensembl(url)

                if not data:
                    html = error_html("API error or species not found")
                else:

                    found = False
                    length = None

                    for c in data.get("top_level_region", []):
                        if c["name"] == chromo:
                            length = c["length"]
                            found = True
                            break

                    if not found:
                        html = error_html("Chromosome not found")
                    else:
                        html = f"""
                        <h1>Chromosome length</h1>
                        <p>Species: {species}</p>
                        <p>Chromosome: {chromo}</p>
                        <p>Length: {length}</p>
                        <a href='/'>Back</a>
                        """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        # DEFAULT
        html = error_html("Endpoint not found")
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


print("Server running on http://localhost:8080")
server = HTTPServer(("", PORT), Server)
server.serve_forever()