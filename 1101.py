while True:
    a, b = map(int, input().split())
    if a == 0 or b == 0 or a < 0 or b < 0:
        break
    sum = 0
    if(a>b):
        for i in range(b,a+1,1):
            print(i,end=" ")
            sum += i
        print(f"Sum={sum}")
    else:
        for i in range(a,b+1,1):
            print(i,end=" ")
            sum += i
        print(f"Sum={sum}")