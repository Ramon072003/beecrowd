diasPrevistos = int(input())
ida = ""
volta = ""
c = 0
e = 0
for i in range(0,diasPrevistos,1):
    ida, volta = input("").split()
    if(ida=="sol" and e==0):
        e +=1
    elif(ida=="chuva" and e===)