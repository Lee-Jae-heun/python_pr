import sys
x = []
y = []
for i in range(3):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i]) == 1:
        x_cnt = x[i]
    if y.count(y[i]) == 1:
        y_cnt = y[i]
print(x_cnt, y_cnt)