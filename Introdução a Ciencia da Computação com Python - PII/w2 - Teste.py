def fazAlgo(string):
    pos = 0
    #string = string.lower()
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        string1 = string1.capitalize()
        pos = pos + 1
    return string1

print(fazAlgo("ISTO É UM TESTE"))
