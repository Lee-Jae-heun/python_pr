import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    stack = 0
    if n != 1:
        for i in range(k):
            cnt = i + 1
            num = 1
            if i == 0:
                stack += i*n
            else:
                for l in range(n):
                    stack += cnt + num
                    num = cnt + num
                    cnt += 1
    else:
        stack = 1*k
    print(stack)