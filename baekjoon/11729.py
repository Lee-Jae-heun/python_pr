import sys
N = int(sys.stdin.readline().rstrip())
def hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)
cnt = 1
for i in range(N):
    cnt *= 2
print(cnt-1)
hanoi(N, 1, 2, 3)