import sys
N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
Max = -1000000
Min = 1000000
if 1 <= N <= 1000000:
    for i in range(N):
        if -1000000 <= a[i] <= 1000000:
            if Max < a[i]:
                Max = a[i]
            if Min > a[i]:
                Min = a[i]
    print(Min, Max)