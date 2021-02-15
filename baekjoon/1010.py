# 다시
import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a1, b1 = 1, 1
    for j in range(1, a+1):
        a1 *= j
    for l in range(1, b+1):
        b1 *= l
    print(a1, b1, a1/b1)
            