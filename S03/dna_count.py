def dna_function(sequence):
    A = 0
    G = 0
    T = 0
    C = 0
    for i in range(0, len(sequence)):
        if sequence[i] == 'A':
            A += 1
        elif sequence[i] == 'G':
            G += 1
        elif sequence[i] == 'T':
            T += 1
        else:
            C += 1
    return A, G, T, C

seq = input("Enter a DNA sequence ")
print(dna_function(seq))
print(len(seq))
