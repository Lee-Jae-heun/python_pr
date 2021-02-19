import sys
n = int(sys.stdin.readline().rstrip())
def fibonacci(N):
    if N == 1 or N == 2:
        return 1
    if N == 0:
        return 0
    return fibonacci(N-1)+fibonacci(N-2)
print(fibonacci(n))