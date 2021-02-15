import sys
T = int(sys.stdin.readline().rstrip())
if T <= 1000000:
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if 1 <= a <= 1000 and 1 <= b <= 1000:
            print(a+b)