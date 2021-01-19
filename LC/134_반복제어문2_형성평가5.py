nums = list(map(int, input().split()))
even, odd = 0, 0
for i in nums:
    if i % 2:
        odd += 1
    else:
        even += 1
print("""even : %d
odd : %d""" %(even, odd))