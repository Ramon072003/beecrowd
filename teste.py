valor = int(input())
lista = []
a = 0

for i in range(valor,0,-1):
    print(i)
    lista.append(i)
print(lista)

for numero in lista:
    if valor%numero == 0:
        a +=1
if a>2:
    print("Not Prime")
else:
    print("Prime")