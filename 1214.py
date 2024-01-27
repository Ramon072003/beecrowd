nTestes = int(input())
somaNotas = 0
qtd = 0

for i in range(0,nTestes,1):
    somaNotas = 0
    qtd = 0
    aprova = -1
    while aprova == -1:
        lista = list(map(int, input().split()))
        alunos = lista[0]
        lista.pop(0)
        if len(lista) > alunos or len(lista) < alunos:
            aprova = -1
        else:
            aprova = 0
    for valor in lista:
        somaNotas += valor
    media = somaNotas/alunos
    for valor in lista:
        if valor > media:
            qtd += 1
    porcentagem = qtd*100/alunos
    arredondado = round(porcentagem, 3)
    print("{:.3f}%".format(arredondado))
