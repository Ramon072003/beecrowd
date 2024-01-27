porcoes = [300,1500,600,1000,150]
gramas = 0
for i in range(0,5,1):
    entrada = int(input())
    gramas += porcoes[i]*entrada

gramas +=225

print(gramas)