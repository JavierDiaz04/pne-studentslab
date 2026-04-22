def main():
    genes = {
        "FRAT1": "ENSG00000165879",
        "ADA": "ENSG00000196839",
        "FXN": "ENSG00000165060",
        "RNU6_269P": "ENSG00000212379",
        "MIR633": "ENSG00000207552",
        "TTTY4C": "ENSG00000228294",
        "RBMY2YP": "ENSG00000227633",
        "FGFR3": "ENSG00000068078",
        "KDR": "ENSG00000128052",
        "ANK2": "ENSG00000145362"
    }

    # 2. Imprimir los encabezados (respetando la errata 'dicctionary' de la imagen)
    print("Dictionary of Genes!")
    print(f"There are {len(genes)} genes in the dicctionary:\n")

    # 3. Recorrer el diccionario e imprimir cada gen con su flecha -->
    # Usamos el método .items() o simplemente iteramos por las llaves
    for name in genes:
        identifier = genes[name]
        print(f"{name}: --> {identifier}")

if __name__ == "__main__":
    main()