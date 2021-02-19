import sys
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
if w - x < x:
    x = w-x
else:
    x = x
if h - y < y:
    y = h-y
else:
    y = y
if y < x:
    print(y)
else:
    print(x)