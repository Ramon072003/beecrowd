def primo(x):
    primos = []
    listNumeros = []
    for i in range(1,x+1,1):
        listNumeros.append(i)

    for valor in listNumeros:
        qtd = 0
        for comparador in listNumeros:
            if(valor%comparador==0):
                qtd += 1
        if(qtd<=2):
            primos.append(valor)

    return primos


N, M = map(int, input().split())
primosN = primo(N)
primosM = primo(M)
valorN = primosN[len(primosN)-1]
valorM = primosM[len(primosM)-1]
print(valorN*valorM)

