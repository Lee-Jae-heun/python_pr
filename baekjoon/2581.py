import sys
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
decimal = []
total = 0
for i in range(M, N+1):
    if i == 0:
        break
    elif i == 2:
        decimal.append(i)
    for j in range(2, i):
        if i%j == 0:
            break
        elif j == i-1:
            decimal.append(i)
for i in decimal:
    total += int(i)
decimal.sort()
if len(decimal) != 0:
    print(total, decimal[0], sep="\n")
else:
    print(-1)