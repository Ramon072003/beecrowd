colocacao = [1, 3, 5, 10, 25, 50, 100]
entrada = float(input())
while(entrada<1 or entrada>100):
    entrada = float(input())
for i in range(0,len(colocacao),1):
    if(entrada<=colocacao[i]):
        print(f"Top {colocacao[i]}")
        break