def hexa_para_decimal(hexa):
    decimal = int(hexa, 16)
    return decimal

def decimal_para_hexa(decimal):
    hexa = hex(decimal)[2:]
    return hexa.upper()

entrada = 0

while entrada != "-1":
    entrada = input()
    if entrada == "-1":
        break
    else:
        entradaList = list(entrada)
        if len(entradaList) > 1:
            if entradaList[1] == "x":
                print(hexa_para_decimal(entrada))
            else:
                print(f"0x{decimal_para_hexa(int(entrada))}")
        else:
            print(f"0x{decimal_para_hexa(int(entrada))}")

