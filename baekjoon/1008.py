import sys
a, b = map(int, sys.stdin.readline().strip().split())
if 0 < a and b < 10:
    print(a/b)