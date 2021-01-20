n = int(input())
total, idx = 0, 0
for i in range(1, n + 1, 2):
    if total < n:
        total += i
        idx += 1
    else:
        print(idx, total)
        break