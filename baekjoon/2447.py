import sys
N = int(sys.stdin.readline().rstrip())
def star(N):
    global map_star
    if N == 3:
        map_star[0][:3] = [1]*3
        map_star[2][:3] = [1]*3
        map_star[1][:3] = [1, 0, 1]
        return
    a = N//3
    star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                map_star[a*i+k][a*j:a*(j+1)] = map_star[k][:a]
map_star = [[0 for i in range(N)] for i in range(N)]
star(N)
for i in map_star:
    for j in i:
        if j:
            print("*", end="")
        else:
            print(" ", end="")
    print()