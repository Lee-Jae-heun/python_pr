import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if 1 <= a < 100 and 1 <= b < 1000000:
        data = a**b
        num = data % 10
        print(num)
    else:
        break