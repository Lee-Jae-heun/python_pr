import sys
N, X = map(int, sys.stdin.readline().rstrip().split())
a = []
if 1 <= N and X <= 10000:
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N):    
        if X > a[i]:
            print("{}".format(a[i]), end=" ")