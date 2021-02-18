import sys
N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for i in num:
    if i == 0:
        pass
    elif i == 2:
        cnt += 1
    for j in range(2, i):
        if i%j == 0:
            break
        elif j == i-1:
            cnt += 1
print(cnt)
