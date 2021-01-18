total, cnt = 0, 0
numbers = list(map(int, input().split()))
for i in numbers:
    cnt += 1
    total += i
    if i >= 100:
        print(total)
        print("%.1f" %(total / cnt))
        break