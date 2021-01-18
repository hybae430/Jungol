n = int(input())
total = 0
scores = list(map(int, input().split()))
avg = round(sum(scores) / n, 1)
print("avg :", avg)
if avg >= 80:
    print("pass")
else:
    print("fail")