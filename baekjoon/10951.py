import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if 0 < a and b < 10:
            print(a+b)
    except:
        break