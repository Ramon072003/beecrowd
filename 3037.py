nTestes = int(input())
ganhadores = []

for _ in range(nTestes):
    resultJoao = 0
    resultMaria = 0

    for _ in range(3):  # Loop para as jogadas de João
        x, d = map(int, input().split())
        resultJoao += x * d

    for _ in range(3):  # Loop para as jogadas de Maria
        x, d = map(int, input().split())
        resultMaria += x * d

    if resultJoao > resultMaria:
        ganhadores.append("JOAO")
    else:
        ganhadores.append("MARIA")

for ganhador in ganhadores:
    print(ganhador)
