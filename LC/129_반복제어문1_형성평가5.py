while 1:
    base = int(input("Base = "))
    height = int(input("Height = "))
    print("Triangle width = %.1f" %(base * height / 2))
    ctn = list(input("Continue? "))
    if (ctn[0] != 'y') and (ctn[0] != 'Y'):
        break