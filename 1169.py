nCasos = int(input(''))

for i in range(0,nCasos,1):
        a = 1
        c = 0
        nCasas = int(input(''))
        for i in range(0,nCasas,1):
            c += a
            b = a*2
            a = b
        kg = (c//12)//1000
        print(f"{kg} kg")



