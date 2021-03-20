n = int(input())
idx = n - 1
for i in range(1, n + 1):
    print('  ' * idx, end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    idx -= 1
    print()