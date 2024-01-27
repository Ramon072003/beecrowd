def is_prime(valor):
    if valor <= 1:
        return "Not Prime"
    if valor <= 3:
        return "Prime"
    if valor % 2 == 0 or valor % 3 == 0:
        return "Not Prime"
    
    i = 5
    while i * i <= valor:
        if valor % i == 0 or valor % (i + 2) == 0:
            return "Not Prime"
        i += 6

    return "Prime"

nTestes = int(input())

for _ in range(nTestes):
    caso = int(input())
    print(is_prime(caso))
