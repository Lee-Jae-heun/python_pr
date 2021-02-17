import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
if b >= c:
    print(-1)
elif a != 0:
    print((a//(c-b))+1)
else:
    print(1)