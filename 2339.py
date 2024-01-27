while True:
    try:
        dados = list(input().split())
        for i in range(0,len(dados),1):
            dados[i] = int(dados[i])
        quantNeed = dados[0]*dados[2]
        if(quantNeed>dados[1]):
            print("N")
        else:
            print("S")
    
    except EOFError:
        break
