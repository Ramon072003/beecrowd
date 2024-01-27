while True:
    try:
        ano = int(input())
        if ano%4==0 and ano%100!=0 or ano%400==0:
            print("This is leap year.")
            if ano%15==0 and ano%55==0:
                print("This is huluculu festival year.")
                print("This is bulukulu festival year.")
                print("")
            elif ano%15==0:
                print("This is huluculu festival year.")
                print("")
            elif ano%55==0:
                print("This is bulukulu festival year.")
                print("")
        elif ano%15==0:
                print("This is huluculu festival year.")
                print("")
        else:
             print("This is an ordinary year.")
             print("")
    except EOFError:
        break