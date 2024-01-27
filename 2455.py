P1, C1, P2, C2 = map(int, input().split())

momento_esquerda = P1 * C1
momento_direita = P2 * C2

if momento_esquerda == momento_direita:
    print('0')
elif momento_esquerda < momento_direita:
    print('1')
else:
    print('-1')
