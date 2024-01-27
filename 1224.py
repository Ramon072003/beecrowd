while True:
    try:    
        nCartoes = int(input())
        cartoes = list(map(int, input().split()))
        a = 0
        w = 0

        # A seguir:
        # Verifica o maior valor da lista
        # Caso as duas extremidades sejam diferentes desse maior valor, o jogador ira pegar o menor valor entre as duas extremidades
        # Assim ele garante que na próxima rodada tenha a possibilidade de pegar o maior valor, impedindo o segundo jogador de pega-lo

        for i in range(0, nCartoes,1):
            maior_lista = max(cartoes)
            if i%2 == 0:
                if cartoes[0]!= maior_lista and cartoes[-1]!= maior_lista:
                    if cartoes[0] < cartoes[-1]:
                        a += cartoes[0]
                        cartoes.pop(0)
                    else:
                        a += cartoes[-1]
                        cartoes.pop(-1)
                elif cartoes[0] == maior_lista:
                    a += cartoes[0]
                    cartoes.pop(0)
                else:
                    a += cartoes[-1]
                    cartoes.pop(-1)
            else:
                if cartoes[0]!= maior_lista and cartoes[-1]!= maior_lista:
                    if cartoes[0] < cartoes[-1]:
                        w += cartoes[0]
                        cartoes.pop(0)
                    else:
                        w += cartoes[-1]
                        cartoes.pop(-1)
                elif cartoes[0] == maior_lista:
                    w += cartoes[0]
                    cartoes.pop(0)
                else:
                    w += cartoes[-1]
                    cartoes.pop(-1)

        print(a)
        
    except EOFError:
        break