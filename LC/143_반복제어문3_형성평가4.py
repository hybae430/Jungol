n = int(input())
idx = 0
for i in range(n, 0 , -1):
    print(' ' * idx + '*' * (2 * i - 1))
    idx += 1
idx -= 2
for i in range(2, n + 1):
    print(' ' * idx + '*' * (2 * i - 1))
    idx -= 1