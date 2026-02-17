# bases = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
f = open("dna.txt", "r")
bases = f.readlines()
f.close()
def function(bases):
    total_bases = 0
    A = 0
    C = 0
    G = 0
    T = 0
    for j in range(0, len(bases)):
# usamos el .strip() para eliminar el endofline character
        length = len(bases[j].strip())
        base = bases[j].strip()
        for i in range(0, length):
            if base[i] == 'A':
                A += 1
            elif base[i] == 'G':
                G += 1
            elif base[i] == 'T':
                T += 1
            else:
                C += 1
            total_bases += 1
    return A, G, T, C, total_bases

print(function(bases)) # para importar funciones de otros files para meterlo en un ejercicio en el que te interese
# meter la funcion y es lo haces con: from la file de la que lo quieras importar import y el nombre de la funcion
# para importar de forma segura lo mejor que puedes hacer es meterlo todo en una funcion y poner if__name__ == "__main()__":
#                                                                                                main()