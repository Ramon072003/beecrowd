while True:
    try:
        friend, enemy = map(int, input().split())
        diferenca = abs(friend-enemy)
        print(diferenca)
    except EOFError:
        break