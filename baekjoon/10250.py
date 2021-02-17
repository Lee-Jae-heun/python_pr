import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    Y = N%H
    X = N//H + 1
    if Y == 0:
        Y = H
        X = N//H
    if X < 10:
        print("{0}0{1}".format(Y, X))
    else:
        print("{0}{1}".format(Y, X))