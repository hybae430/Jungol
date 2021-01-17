y = int(input())
if (not y % 400) or (not y % 4 and y % 100):
    print('leap year')
else:
    print('common year')