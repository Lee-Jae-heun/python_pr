import sys
N = int(sys.stdin.readline().rstrip())
a = N // 5
b = N // 3
Min = 100000
for i in range(a+1):
    for j in range(b+1):
        if i*5 + j*3 == N:
            if Min > i+j:
                Min = i+j
if Min == 100000:
    print(-1)
else:
    print(Min)