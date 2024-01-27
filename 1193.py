def binario_para_decimal(binario):
    decimal = int(binario, 2)
    return decimal

def binario_para_hexa(binario):
    decimal = int(binario, 2)
    hexa = hex(decimal)[2:]  # O [2:] remove o prefixo '0x'
    return hexa.upper()

def decimal_para_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

def decimal_para_hexa(decimal):
    hexa = hex(decimal)[2:]
    return hexa.upper()

def hexa_para_binario(hexa):
    decimal = int(hexa, 16)
    binario = bin(decimal)[2:]
    return binario

def hexa_para_decimal(hexa):
    decimal = int(hexa, 16)
    return decimal

nTestes = int(input())

for i in range(nTestes):
    valor, tipo = input().split()
    
    if tipo == "bin":
        valor_convert_decimal = binario_para_decimal(valor)
        valor_convert_hexa = binario_para_hexa(valor)
        print(f"Case {i+1}:")
        print(f"{valor_convert_decimal} dec")
        print(f"{valor_convert_hexa} hex")
        print("")
    
    elif tipo == "dec":
        valor_convert_binario = decimal_para_binario(int(valor))
        valor_convert_hexa = decimal_para_hexa(int(valor))
        print(f"Case {i+1}:")
        print(f"{valor_convert_hexa} hex")
        print(f"{valor_convert_binario} bin")
        print("")

    else:
        valor_convert_decimal = hexa_para_decimal(valor)
        valor_convert_binario = hexa_para_binario(valor)
        print(f"Case {i+1}:")
        print(f"{valor_convert_decimal} dec")
        print(f"{valor_convert_binario} bin")
        print("")
