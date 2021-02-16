import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
result = a*b*c
result = str(result)
for _ in range(10):
    print(result.count("{}".format(_)))