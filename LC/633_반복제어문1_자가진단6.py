while 1:
    i = int(input("""1. Korea
2. USA
3. Japan
4. China
number? """))
    print()
    if i == 1:
        print("Seoul\n")
    elif i == 2:
        print("Washington\n")
    elif i == 3:
        print("Tokyo\n")
    elif i == 4:
        print("Beijing\n")
    else:
        print("none")
        break