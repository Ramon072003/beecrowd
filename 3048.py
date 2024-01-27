numeroDeEntradas = int(input())
listaMisterio = []
valoresCirculados = 0
for i in range(0,numeroDeEntradas,1):
    entrada = int(input())
    listaMisterio.append(entrada)

i = 0
while(i<=numeroDeEntradas):
    if(i+1<numeroDeEntradas):
        if(listaMisterio[i]!=listaMisterio[i+1]):
            valoresCirculados +=1
    i+=1
valoresCirculados +=1

print(valoresCirculados)
