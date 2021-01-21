total, idx = 0, 0
nums = list(map(int, input().split()))
for n in nums:
    if n != 0 or idx != 20:
        total += n
        idx += 1
    else:
        print(total, round(total // idx))
        break