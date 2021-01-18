numbers = list(map(int, input().split()))
three, five = 0, 0
for i in numbers:
    if i and not i % 3:
        three += 1
    if i and not i % 5:
        five += 1
print("""Multiples of 3 : %d
Multiples of 5 : %d""" %(three, five))