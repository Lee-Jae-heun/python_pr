import sys
N = int(sys.stdin.readline().rstrip())
score = []
score = list(map(int, sys.stdin.readline().rstrip().split()))
Max_score = 0
total = 0
for i in range(N):
    if Max_score < score[i]:
        Max_score = score[i]
for i in range(N):
    total += score[i]/Max_score*100
print(total/N)
