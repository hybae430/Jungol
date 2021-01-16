h, w = map(int, input().split())
o = w + 100 - h
print(o)
if o > 0:
    print("Obesity")