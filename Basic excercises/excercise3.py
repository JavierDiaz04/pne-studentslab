def average(temperatures):
    total = 0
    for i in temperatures:
        total = total + i
    return total/len(temperatures)

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
c = 0
for i in temperatures:
    if i > 17:
        c += 1
print(c)
ordered_temperatrures = sorted(temperatures)
print(ordered_temperatrures)
print(temperatures[2])
print(max(temperatures))
print(min(temperatures))
print(average(temperatures))

