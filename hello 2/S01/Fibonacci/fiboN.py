def fibon(n):
    a, b = 0, 1
    for i in range(n):
        a , b = b, a + b
    return a

print(fibon(5))
print(fibon(10))
print(fibon(15))