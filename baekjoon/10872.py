import sys
N = int(sys.stdin.readline().rstrip())
total = 1
def factorial(N):
    global total
    if N == 0:
        return total
    total *= N
    N -= 1
    return factorial(N)
print(factorial(N))