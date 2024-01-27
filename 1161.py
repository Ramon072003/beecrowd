def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

while True:
    try:
        a, b = map(int,input().split())
        fatorialA = fatorial(a)
        fatorialB = fatorial(b)
        soma = fatorialA+fatorialB
        print(int(soma))
    except EOFError:
        break