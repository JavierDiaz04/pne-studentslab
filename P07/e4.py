import http.client
import json


# Minimal Seq class based on Exercise 4 requirements
class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases

    def len(self):
        return len(self.str_bases)

    def count(self, base):
        return self.str_bases.count(base)

    def percentage(self, base):
        return (self.count(base) / self.len()) * 100

    def most_frequent(self):
        bases = ['A', 'C', 'G', 'T']
        counts = {b: self.count(b) for b in bases}
        return max(counts, key=counts.get)


# Dictionary from Exercise 2
genes = {
    "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228294",
    "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"
}


def main():
    # User input
    name = input("Write the gene name: ").strip().upper()

    if name not in genes:
        print("Gene not found.")
        return

    stable_id = genes[name]
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/sequence/id/{stable_id}'
    PARAMS = '?content-type=application/json'

    print(f"\nServer: {SERVER}")
    print(f"URL: {SERVER}{ENDPOINT}{PARAMS}")

    # Connection and Request
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", ENDPOINT + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")

        if r1.status == 200:
            data = r1.read().decode()
            gene_data = json.loads(data)

            # Sequence Processing
            sequence = gene_data['seq']
            description = gene_data.get('desc', 'No description')
            my_seq = Seq(sequence)

            # Printing Results
            print(f"Gene: {name}")
            print(f"Description: {description}")
            print("New sequence created!")
            print(f"Total lengh: {my_seq.len()}")  # Note: Professor uses 'lengh' typo

            for base in ['A', 'C', 'G', 'T']:
                cnt = my_seq.count(base)
                pct = my_seq.percentage(base)
                print(f"{base}: {cnt} ({pct:.1f}%)")

            print(f"Most frequent Base: {my_seq.most_frequent()}")

    except Exception as e:
        print(f"ERROR! {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()