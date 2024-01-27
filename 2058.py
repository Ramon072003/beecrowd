while True:
    lados = float(input())
    if(lados<3 or lados>1000000000):
        continue
    else:
        break

triangulos = "{:.0f}".format(lados-2)
print(triangulos)