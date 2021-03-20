n = int(input())
num, alpha = 0, 0
for i in range(n):
    for x in range(alpha, alpha + n):
        print(chr(65 + x), end=" ")
    for x in range(num, num + alpha):
        print(x, end=" ")
    alpha += n
    num += 1
    print()