a, b = map(int, input().split())
total, cnt = 0, 0
for i in range(min(a, b), max(a, b) + 1):
    if i and (i % 3 == 0 or i % 5 == 0):
        total += i
        cnt += 1
print("""sum : %d
avg : %.1f""" %(total, total / cnt))