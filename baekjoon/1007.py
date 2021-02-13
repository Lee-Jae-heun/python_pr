import sys
import math
import itertools
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    x_total = 0
    y_total = 0
    coords = []
    if N%2 != 0 or N <= 0 or N > 20:
        break
    for j in range(1, N+1):
        x, y = map(int, sys.stdin.readline().rstrip().rsplit())
        x_total += x
        y_total += y
        coords.append([x, y])
    Veoter = 3.4E+38
    combinations = list(itertools.combinations(coords, int(N/2))) #조합의 수를 튜플로 변환
    combinations_lens_half = int(len(combinations)/2)
    for sum_coord in combinations[:combinations_lens_half]:
        sum_coord = list(sum_coord)

        x1_total = 0
        y1_total = 0
        for x1, y1 in sum_coord:
            x1_total += x1
            y1_total += y1

        x2_total = x_total - x1_total
        y2_total = y_total - y1_total

        Veoter = min(Veoter, ((x1_total - x2_total)**2 +(y1_total - y2_total)**2)**0.5)
    print(Veoter)