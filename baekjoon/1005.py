# 위상 정렬, 큐 개념
import sys
T = int(sys.stdin.readline().rstrip())
i = 0

for i in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().rsplit())
    Delay = []
    routes = [[] for _ in range(K)]
    dots = [[] for _ in range(K)] #각 건물들이 가르키고 있는 다음 건물
    cnt = [0] * (K)               #건물들의 진입차수(자신을 가리키는 화살표의 개수)
    queue = []
    result = [0] * (K)
    Delay = list(sys.stdin.readline().rstrip().rsplit())

    for j in range(K):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        dots[a-1].append(b)
        routes[b-1].append(a)

    W = int(sys.stdin.readline().rstrip())
    
    for l in range(K):
        cnt[l] = len(routes[l])

    while True:
        if cnt[W-1] != 0:
            for m in range(K):
                if cnt[m] == 0:
                    queue.append(m)
            if len(queue) == 0:
                break
            node = queue.pop(0)
        else:
            node = W-1

        max_delay = 0
        for routes_node in routes[node]:
            if result[routes_node-1] > max_delay:
                max_delay = result[routes_node-1]
        result[node] = int(max_delay) + int(Delay[node])

        if node == W:
            break

        cnt[node] = -1
        for s in dots[node]:
            cnt[s-1] -= 1
    print(result[W-1])