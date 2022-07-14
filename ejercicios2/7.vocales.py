palabra = "Juan"
vocal = 0

for x in palabra:
    y = x.lower()
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
        vocal += 1

print(vocal)