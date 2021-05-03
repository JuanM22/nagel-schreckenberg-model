lista = []

lista += [None] * 5

print(len(lista))
print(len(list(filter(None, lista))))
print(len(lista))
