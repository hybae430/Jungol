numbers = list(map(int, input().split()))
total, cnt = 0, 0
for i in numbers:
    if i < 0 or i > 100:
        print("""sum : %d
avg : %.1f""" %(total, total / cnt))
    else:
        total += i
        cnt += 1