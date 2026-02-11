def function(string):
    a = len(string)
    c = string[18 : 21]
    b = string[0 : 4]
    d = string.lower()
    subsequence = string.count("ATC")
    new_string = string.replace("T", "U")
    return a, b, c, d, subsequence, new_string


string = "ATGCGATCGATCGATCGATCGA"
print(function(string))