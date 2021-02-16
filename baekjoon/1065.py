import sys
def solve(num, cnt):
    if num < 100:
        cnt += 1
    else:
        num = str(num)
        if int(num[0]) + int(num[2]) == int(num[1])*2:
            cnt += 1
    return cnt
N = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range(1, N+1):
    cnt = solve(i, cnt)
print(cnt)