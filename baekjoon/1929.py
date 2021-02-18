import sys
M, N = map(int, sys.stdin.readline().rstrip().split())
decimal = [i for i in range(0, N+1)]
for i in range(1, N+1):
    cnt = 2
    if decimal[i] == 0:
        continue
    while i*cnt <= N:
        if i == 1:
            decimal[1] = 0
            break
        else:
            decimal[i*cnt] = 0
            cnt += 1
for i in range(M, N+1):
    if decimal[i] != 0:
        print(decimal[i])