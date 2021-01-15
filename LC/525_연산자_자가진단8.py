a, b, c = map(int, input().split())
print(1 if (a > b) & (a > c) else 0, end=" ")
print(1 if a == b == c else 0)