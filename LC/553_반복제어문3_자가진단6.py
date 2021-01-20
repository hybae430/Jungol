n =int(input())
i = 0
for x in range(n, 0, -1):
    for y in range(1, x + 1):
      print(chr(65 + i), end='')
      i += 1
    print()