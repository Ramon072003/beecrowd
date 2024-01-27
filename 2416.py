dados = list(map(int,input().split()))
voltas = dados[0]//dados[1]
pontoFinal = dados[0]-(voltas*dados[1])

print(pontoFinal)