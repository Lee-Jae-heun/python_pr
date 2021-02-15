import sys
while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if 0 < a and b < 10:
        print(a+b)
    else:
        break