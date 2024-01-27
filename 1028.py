import math

def mdc(a,b):
    mdc = math.gcd(a, b)
    return mdc

nCasos = int(input())
for i in range(0,nCasos,1):
    pausador = 0
    qtd1, qtd2 = map(int, input().split())
    print(mdc(qtd1,qtd2))
                
