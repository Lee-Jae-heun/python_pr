import sys
remains = set()
for _ in range(10):
    a = int(sys.stdin.readline().rstrip())
    if 0 <= a <= 1000:
        remain = a%42
        remain = str(remain)
        remains.add(remain)
print(len(remains))