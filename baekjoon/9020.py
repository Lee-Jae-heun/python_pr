import sys
decimal = [0]*(10002)
sosu = []
for i in range(2, 10001):
    cnt = 2
    while i*cnt <= 10001:
        decimal[i*cnt] = 1
        cnt += 1
for i in range(2, 10001):
    if decimal[i] == 0:
        sosu.append(i)
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    a = N//2
    breaker = False
    for i in range(len(sosu)):
        if sosu[i] >= a:
            a = i
            break
    for i in range(a, -1, -1):
        for j in range(a, len(sosu)):
            if sosu[i] + sosu[j] == N:
                print(sosu[i], sosu[j])
                breaker = True
                break
        if breaker == True:
            break