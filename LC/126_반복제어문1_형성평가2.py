numbers = list(map(int, input().split()))
odd, even = 0, 0
for i in numbers:
    if not i:
        print("""odd : %d
even : %d""" %(odd, even))
    elif i % 2:
        odd += 1
    else:
        even += 1