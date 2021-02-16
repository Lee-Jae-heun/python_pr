import sys
T = int(sys.stdin.readline().rstrip())
i = 0
cnt = 0
while i < T:
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().rsplit())
    n = int(sys.stdin.readline().rstrip())
    j = 0
    while j < n:
        Cx, Cy, r = map(int, sys.stdin.readline().rstrip().rsplit())
        z1 = ((x1 - Cx)**2 + (y1 - Cy)**2)**0.5
        z2 = ((x2 - Cx)**2 + (y2 - Cy)**2)**0.5
        if z1 < r:
            cnt += 1
        if z2 < r:
            cnt += 1
        j += 1
    print("{0}".format(cnt))
    cnt = 0
    i += 1