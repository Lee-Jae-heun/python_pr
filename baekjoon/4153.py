import sys
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    Max = 0
    if a == 0 and b == 0 and c == 0:
        break
    if Max < a:
        Max = a
    if Max < b:
        Max = b
    if Max < c:
        Max = c
    if Max == a and c**2 + b**2 == a**2:
        print("right")
    elif Max == b and c**2 + a**2 == b**2:
        print("right")
    elif Max == c and a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")