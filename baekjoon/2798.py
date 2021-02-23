import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
card = []
card = list(map(int, sys.stdin.readline().rstrip().split()))
Max = 0
for i in range(N):
    for j in range(i):
        for l in range(j):
            if card[i] + card[j] + card[l] <= M and card[i] + card[j] + card[l] > Max:
                Max = card[i] + card[j] + card[l]
print(Max)