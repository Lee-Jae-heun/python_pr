import sys
N = int(sys.stdin.readline().rstrip())
if 1 <= N <= 100:
    for i in range(1, N+1):
        print(" "*(N-i),"*"*i, sep="")