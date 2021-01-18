while 1:
    i = int(input())
    if i == -1:
        break
    if not i % 3:
        print(i // 3)