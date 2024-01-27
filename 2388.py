total = 0
qtdIntervalos = int(input())
for i in range(0,qtdIntervalos,1):
    intervalos = list(map(int, input().split()))
    km = intervalos[0]*intervalos[1]
    total += km
    
print(total)