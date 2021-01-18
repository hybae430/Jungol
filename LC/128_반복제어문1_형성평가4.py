numbers = list(map(int, input().split()))
cnt = 0
for i in numbers:
    if not i:
        print(cnt)
        break
    elif not i % 3 or not i % 5:
        pass
    else:
        cnt += 1