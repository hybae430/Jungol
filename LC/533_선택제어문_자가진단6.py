g, a = input().split()
if g == "F":
    if int(a) >= 18:
        print("WOMAN")
    else:
        print("GIRL")
else:
    if int(a) >= 18:
        print("MAN")
    else:
        print("BOY")