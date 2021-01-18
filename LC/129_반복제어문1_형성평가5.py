while 1:
    base = int(input("Base = "))
    height = int(input("Height = "))
    print("Triangle width = %.1f" %(base * height / 2))
    ctn = input("Continue? ")
    print(ctn)
    if (ctn != 'y') and (ctn != 'Y'):
        break