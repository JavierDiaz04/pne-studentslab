from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import json

PORT = 8080



MAIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Genome Browser</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f0f0f0;
            margin: 40px;
        }

        h1 {
            color: darkblue;
        }

form {
    background-color: white;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 10px;
}

input[type=text], input[type=number] {
    padding: 5px;
    margin: 5px;
}

input[type=submit] {
    padding: 8px;
    background-color: darkblue;
    color: white;
    border: none;
    border-radius: 5px;
}

.result {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
             }
    </style>
</head>

<body>

<h1>Browsing Human and Vertebrates Genome</h1>

<form action="/listSpecies" method="get">
    <h2>List Species</h2>
    Limit:
    <input type="number" name="limit">
    <input type="submit" value="Get Species">
</form>

<form action="/karyotype" method="get">
    <h2>Karyotype</h2>
    Species:
    <input type="text" name="species">
    <input type="submit" value="Get Karyotype">
</form>

<form action="/chromosomeLength" method="get">
    <h2>Chromosome Length</h2>
    Species:
    <input type="text" name="species">

    Chromosome:
    <input type="text" name="chromo">

    <input type="submit" value="Get Length">
</form>

</body>
</html>
"""


def error_page(message):
    return f"""
    <html>
    <body style="font-family:Arial">
        <h1 style="color:red">ERROR</h1>
        <p>{message}</p>
    </body>
    </html>
    """




class GenomeHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)


        if path == "/":

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(MAIN_PAGE.encode())


        elif path == "/listSpecies":

            url = "https://rest.ensembl.org/info/species?content-type=application/json"

            response = requests.get(url)

            if response.status_code != 200:
                html = error_page("Could not connect to Ensembl API")

            else:
                data = response.json()

                species_list = data["species"]

                limit = None

                if "limit" in params:
                    try:
                        limit = int(params["limit"][0])
                    except:
                        limit = None

                html = """
                <html>
                <body style="font-family:Arial">
                <h1>Species List</h1>
                <ul>
                """

                count = 0

                for sp in species_list:

                    html += f"<li>{sp['display_name']}</li>"

                    count += 1

                    if limit and count >= limit:
                        break

                html += """
                </ul>
                <a href="/">Back</a>
                </body>
                </html>
                """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode())


        elif path == "/karyotype":

            if "species" not in params:
                html = error_page("Missing species parameter")

            else:

                species = params["species"][0]

                url = f"https://rest.ensembl.org/info/assembly/{species}?content-type=application/json"

                response = requests.get(url)

                if response.status_code != 200:
                    html = error_page("Species not found")

                else:

                    data = response.json()

                    if "karyotype" not in data:
                        html = error_page("No karyotype available")

                    else:

                        html = f"""
                        <html>
                        <body style="font-family:Arial">
                        <h1>Karyotype of {species}</h1>
                        <ul>
                        """

                        for chrom in data["karyotype"]:
                            html += f"<li>{chrom}</li>"

                        html += """
                        </ul>
                        <a href="/">Back</a>
                        </body>
                        </html>
                        """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode())


        elif path == "/chromosomeLength":

            if "species" not in params or "chromo" not in params:
                html = error_page("Missing parameters")

            else:

                species = params["species"][0]
                chromo = params["chromo"][0]

                url = f"https://rest.ensembl.org/info/assembly/{species}?content-type=application/json"

                response = requests.get(url)

                if response.status_code != 200:
                    html = error_page("Species not found")

                else:

                    data = response.json()

                    found = False
                    length = 0

                    for chrom in data["top_level_region"]:

                        if chrom["name"] == chromo:
                            length = chrom["length"]
                            found = True
                            break

                    if not found:
                        html = error_page("Chromosome not found")

                    else:

                        html = f"""
                        <html>
                        <body style="font-family:Arial">
                        <h1>Chromosome Length</h1>

                        <p>
                        Species: <b>{species}</b>
                        </p>

                        <p>
                        Chromosome: <b>{chromo}</b>
                        </p>

                        <p>
                        Length: <b>{length}</b>
                        </p>

                        <a href="/">Back</a>

                        </body>
                        </html>
                        """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode())

        # ---------------------------------------------
        # INVALID ENDPOINT
        # ---------------------------------------------
        else:

            html = error_page("Endpoint not found")

            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode())


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

print(f"Server running on port {PORT}...")

server = HTTPServer(("", PORT), GenomeHandler)

server.serve_forever()