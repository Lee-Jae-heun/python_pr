import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    apart = [[0 for col in range(15)] for row in range(15)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                apart[i][j] = j+1
            else:
                if j == 0:
                    apart[i][j] = 1
                else:
                    apart[i][j] = apart[i][j-1] + apart[i-1][j]
    print(apart[k][n-1])