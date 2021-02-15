import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0
N_F = N
if 0 <= N <= 99:
    while True:
        N_1 = N % 10
        N_2 = ((N//10)+(N%10))%10
        N = str(N_1) + str(N_2)
        N = int(N)
        cnt += 1
        if N == N_F:
            break
    print(cnt)