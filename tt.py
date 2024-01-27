def max_pontos(cartoes):
    n = len(cartoes)
    dp = [0] * n

    for intervalo in range(1, n + 1):
        dp_anterior = dp.copy()
        for i in range(n - intervalo + 1):
            j = i + intervalo - 1
            dp[i] = max(cartoes[i] - dp_anterior[i + 1], cartoes[j] - dp[i])

    return dp[0]

while True:
    try:
        nCartoes = int(input())
        cartoes = list(map(int, input().split()))

        resultado = max_pontos(cartoes)
        print(resultado)

    except EOFError:
        break
