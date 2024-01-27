nCasos = int(input())

for i in range(0,nCasos,1):
    j = 0
    comida = float(input())
    while comida > 1:
        comida /= 2
        j += 1
    print(f"{j} dias")
