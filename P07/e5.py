import http.client
import json


# Reutilizamos la clase Seq para los cálculos de bases
class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases

    def len(self):
        return len(self.str_bases)

    def count(self, base):
        return self.str_bases.count(base)

    def percentage(self, base):
        length = self.len()
        return (self.count(base) / length) * 100 if length > 0 else 0

    def most_frequent(self):
        bases = ['A', 'C', 'G', 'T']
        counts = {b: self.count(b) for b in bases}
        return max(counts, key=counts.get)


def main():
    # Diccionario de genes definido en el Ejercicio 2
    GENES = {
        "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
        "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379",
        "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228294",
        "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
        "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"
    }

    SERVER = 'rest.ensembl.org'
    PARAMS = '?content-type=application/json'

    # Iteramos por cada nombre en el diccionario
    for name in GENES:
        stable_id = GENES[name]
        ENDPOINT = f'/sequence/id/{stable_id}'
        REQ = ENDPOINT + PARAMS
        URL = SERVER + REQ

        print(f"\nServer: {SERVER}")
        print(f"URL: {URL}")

        # Conexión con el servidor Ensembl
        conn = http.client.HTTPSConnection(SERVER)

        try:
            conn.request("GET", REQ)
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")

            if r1.status == 200:
                data1 = r1.read().decode()
                gene_json = json.loads(data1)  # Cargamos el cuerpo de la respuesta

                # Procesamiento con la clase Seq
                sequence_text = gene_json['seq']
                description = gene_json.get('desc', 'No description')
                my_seq = Seq(sequence_text)

                # Salida de datos formateada
                print(f"Gene: {name}")
                print(f"Description: {description}")
                print("New sequence created!")
                print(f"Total lengh: {my_seq.len()}")  # Mantenemos la errata 'lengh'

                for base in ['A', 'C', 'G', 'T']:
                    cnt = my_seq.count(base)
                    pct = my_seq.percentage(base)
                    print(f"{base}: {cnt} ({pct:.1f}%)")

                print(f"Most frequent Base: {my_seq.most_frequent()}")
                print("-" * 30)  # Separador visual entre genes

        except Exception as e:
            print(f"ERROR! Cannot connect to the Server: {e}")

        finally:
            conn.close()


if __name__ == "__main__":
    main()