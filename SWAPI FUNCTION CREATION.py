def swapi(n):
    k = ''
    for i in n:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    return k


d = input("Enter the word")
print(swapi(d))
