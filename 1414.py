while True:
    T, N = map(int, input().split())
    
    if T == 0:
        break

    totalPoints = 3 * N
    matchDraw = 0

    for i in range(T):
        str, point = input().split()
        point = int(point)
        matchDraw += point

    print(totalPoints - matchDraw)
