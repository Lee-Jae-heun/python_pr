import sys
T = int(sys.stdin.readline().rstrip())
i = 0
while i < T:
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    z1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    z2 = r1 + r2
    if z1 > z2 and z1 != 0:
        print("0")
    elif z1 == z2 and z1 != 0:
        print("1")
    elif z1 < z2 and z1 != 0:
        print("2")
    elif z1 == 0 and r1 != r2:
        print("0")
    else:
        print("-1")
    i += 1