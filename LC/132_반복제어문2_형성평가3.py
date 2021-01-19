i = int(input())
total, index = 0, 1
while i >= 5 * index:
    total += 5 * index
    index += 1
print(total)