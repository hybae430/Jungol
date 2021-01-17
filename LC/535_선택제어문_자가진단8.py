grade = float(input())
if grade < 2.0:
    print('retake')
elif grade < 3.0:
    print('seasonal semester')
elif grade < 4.0:
    print('next semester')
else:
    print('scholarship')