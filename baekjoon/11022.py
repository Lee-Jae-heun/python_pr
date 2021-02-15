import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if 0 < a and b < 10:
        print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))