w, h = map(int, input().split())
w += 5
h *= 2
print("""width = %d
length = %d
area = %d""" %(w, h, w * h))