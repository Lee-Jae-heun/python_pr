import sys
decimal = [0]*(123456*2+1)
sosu = []
for i in range(2, 123456*2+1):
    cnt = 2
    while i*cnt <= 123456*2+1:
        decimal[i*cnt] = 1
        cnt += 1
for i in range(2, 123456*2+1):
    if decimal[i] == 0:
        sosu.append(i)
while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    cnt = 0
    for i in range(0, len(sosu)):
        if N < sosu[i] <= N*2:
            cnt += 1
        elif sosu[i] > N*2:
            break
    print(cnt)