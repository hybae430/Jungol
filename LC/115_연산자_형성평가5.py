mh, mw = map(int, input().split())
gh, gw = map(int, input().split())
print(1 if (mh > gh) & (mw > gw) else 0)