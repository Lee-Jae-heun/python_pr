import sys
a, b = list(sys.stdin.readline().rstrip().split())
aa = a[2] + a[1] + a[0]
bb = b[2] + b[1] + b[0]
aa = int(aa)
bb = int(bb)
if aa > bb:
    print(aa)
else:
    print(bb)