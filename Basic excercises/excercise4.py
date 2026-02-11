def scores(score):
    if score >= 9.0:
        result = "A"
    elif 7.0 <= score < 8.9:
        result = "B"
    elif 5.0 <= score < 6.9:
        result = "C"
    elif 3.0 <= score < 4.9:
        result = "D"
    else:
        result = "F"
    return result

print(scores(9.5))
print(scores(7.0))
print(scores(5.5))
print(scores(3.2))
print(scores(1.0))