import sys
C = int(sys.stdin.readline().rstrip())
N = []
for _ in range(C):
    N = list(map(int, sys.stdin.readline().rstrip().split()))
    total = 0
    cnt = 0
    for i in range(N[0]):
        total += N[i+1]
    mean = total/N[0]
    for i in range(N[0]):
        if mean < N[i+1]:
            cnt += 1
    print("%0.3f%%"% round(cnt/N[0]*100, 3))