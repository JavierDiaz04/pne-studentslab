def fibon(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        a , b = b, a + b
    return a

def fibosum(n):
    total = 0
    for i in range(1, n+1):
        total += fibon(i)
    return total
print(fibosum(5))
print(fibosum(10))
