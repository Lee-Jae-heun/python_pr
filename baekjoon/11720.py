import sys
N = int(sys.stdin.readline().rstrip())
num = str(sys.stdin.readline().rstrip())
sum_ = 0
for _ in range(N):
    sum_ += int(num[_])
print(sum_)