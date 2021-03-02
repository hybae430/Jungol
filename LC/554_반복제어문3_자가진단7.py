n = int(input())
first, idx, alpha = 1, 0, 1
for i in range(n):
    for x in range(first, first + n - idx):
        print(x, end=" ")
    for y in range(alpha, alpha + idx + 1):
        print(chr(y + 64), end=" ")
    print()
    first += n - idx
    idx += 1
    alpha += idx