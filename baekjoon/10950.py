import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if 0 < a and b < 10:
        print("{}".format(a+b))