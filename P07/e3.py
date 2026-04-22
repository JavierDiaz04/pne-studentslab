import http.client
import json


def main():
    # 1. Definición de variables de conexión
    SERVER = 'rest.ensembl.org'
    # Usamos el ID del gen MIR633 obtenido en el Ejercicio 2
    GENE_ID = 'ENSG00000207552'
    ENDPOINT = f'/sequence/id/{GENE_ID}'
    PARAMS = '?content-type=application/json'
    URL = SERVER + ENDPOINT + PARAMS

    # Imprimir información inicial
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    # 2. Establecer conexión HTTPS
    conn = http.client.HTTPSConnection(SERVER)

    try:
        # Realizar la petición GET
        conn.request("GET", ENDPOINT + PARAMS)

        # Obtener respuesta
        res = conn.getresponse()
        print(f"Response received!: {res.status} {res.reason}")

        # 3. Procesar los datos si la respuesta es exitosa (200 OK)
        if res.status == 200:
            data = res.read().decode("utf-8")
            response = json.loads(data)

            # Extraer la descripción y la secuencia (bases) del JSON
            # En Ensembl, los campos suelen ser 'desc' y 'seq'
            gene_name = "MIR633"
            description = response.get('desc', 'No description found')
            bases = response.get('seq', 'No sequence found')

            # Imprimir los resultados con el formato solicitado
            print(f"\nGene: {gene_name}")
            print(f"Description: {description}")
            print(f"Bases: {bases}")
        else:
            print(f"Error: Unexpected status {res.status}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Cerrar conexión
        conn.close()


if __name__ == "__main__":
    main()