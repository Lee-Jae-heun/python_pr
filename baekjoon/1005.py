# 위상 정렬, 큐 개념
import sys
T = int(sys.stdin.readline().rstrip())
i = 0

while i < T:
    N, K = map(int, sys.stdin.readline().rstrip().rsplit())
    j = 0
    D = []
    tree = []
    D = list(sys.stdin.readline().rstrip().rsplit())
    while j < K:
        tree.append(list(sys.stdin.readline().rstrip().split()))
        j += 1
    W = int(sys.stdin.readline().rstrip())
    print(D)
    print(tree)
    i += 1


##########################################



from collections import deque

N = 6 #점의 개수
routes = [[1, 2], [2, 3], [4, 3], [5, 3], [6, 5]] # 앞 원소에서 뒷 원소를 향하는 간선들
dots = [[] for _ in range(N + 1)] #각 점들이 가리키고 있는 점들(후순위에 있는 점들)
cnt = [0] * (N + 1) #점들의 진입차수
for route in routes:
    a, b = route
    dots[a].append(b)
    cnt[b] += 1

#스택 이용
stack = [1, 4, 6]
answer = []
while stack:
    target = stack.pop()
    answer.append(target)
    for dot in dots[target]:
        cnt[dot] -= 1
        if cnt[dot] == 0:
            stack.append(dot)
print(answer)
#answer = [6, 5, 4, 1, 2, 3]

for route in routes:
    a, b = route
    cnt[b] += 1

#큐 이용
queue = deque([1, 4, 6])
answer = []
while queue:
    target = queue.popleft()
    answer.append(target)
    for dot in dots[target]:
        cnt[dot] -= 1
        if cnt[dot] == 0:
            queue.append(dot)
print(answer)
#answer = [1, 4, 6, 2, 5, 3]