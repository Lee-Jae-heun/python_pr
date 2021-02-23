import sys
N = int(sys.stdin.readline().rstrip())
profile = []*N
for _ in range(N):
    profile[_] = list(map(int, sys.stdin.readline().rstrip().split()))
print(profile)