dados = list(map(int,input().split()))
for i in range(0,dados[0]+1,1):
        if(i==0):
            menorValor = dados[1]
        else:
            entrada = int(input())
            dados[1] = entrada+dados[1]
            if(dados[1]<menorValor):
                menorValor = dados[1]

print(menorValor)


