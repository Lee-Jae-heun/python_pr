import sys
T = int(sys.stdin.readline().rstrip())
a = []
for _ in range(T):
    a = str(sys.stdin.readline().rstrip())
    cnt = 0
    total = 0
    for i in range(len(a)):
        if a[i] == "O":
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)