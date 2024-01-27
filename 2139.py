while True:
    try:
        def diasNatal(mes, dia):
            natal = 360
            somaDias = 0
            mesesDias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for i in range(0, mes - 1, 1):
                somaDias += mesesDias[i]
            diasRestanteNoMes = somaDias + dia
            diasNatal = natal - diasRestanteNoMes
            return diasNatal
        
        mes, dia = map(int, input().split())
        diasNatal = diasNatal(mes, dia)
        if diasNatal == 0:
            print("E natal!")
        elif diasNatal == 1:
            print("E vespera de natal!")
        elif diasNatal < 1:
            print("Ja passou!")
        else:
            print(f"Faltam {diasNatal} dias para o natal!")
    except EOFError:
        break