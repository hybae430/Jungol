from datetime import datetime

now = datetime.now()
a = 0
print(a, end=" ")
a = now.year - 1900
print(a, end=" ")
a += now.month - 1
a += now.day
print(a)