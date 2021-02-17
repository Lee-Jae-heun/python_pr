import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    k = [0, 1, 2]
    cnt = 1
    a = y-x-1
    