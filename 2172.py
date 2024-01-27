while True:
    xp = list(map(float,input().split()))
    if(xp[0]==0 and xp[1]==0):
        break
    else:
        newXp = "{:.0f}".format(xp[0]*xp[1])
        print(f"{newXp}")