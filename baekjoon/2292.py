import sys
N = int(sys.stdin.readline().rstrip())
Min = 1
Max = 1
cnt = 1
add = 6
while True:
    if Min <= N <= Max:
        break
    Min = Max + 1
    Max += add 
    add += 6
    cnt += 1
print(cnt)