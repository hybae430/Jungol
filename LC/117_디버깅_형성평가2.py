import math
a, b, c = map(float, input().split())
print("""sum %d
avg %d""" %(math.floor(a) + math.floor(b) + math.floor(c), (a + b + c) / 3))