n = int(input())
idx = n - 1
for i in range(1, n + 1):
    print('  ' * idx + '*' * (i * 2 - 1))
    idx -= 1