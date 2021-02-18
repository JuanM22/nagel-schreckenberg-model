lista = [1,2,3,4,5,0,6]

print(lista)

item = lista.__getitem__(5)

lista[5] = lista[2]
lista[2] = item

print(lista)
