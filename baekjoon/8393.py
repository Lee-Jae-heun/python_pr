n = int(input())
total = 0
if 1 <= n <= 10000:
    for i in range(1, n+1):
        total += i
    print(total)