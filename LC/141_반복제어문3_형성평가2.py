n = int(input())
for i in range(1, 11):
    if n * i < 100:
        print(n * i, end=" ")
    if not (n * i) % 10:
        break