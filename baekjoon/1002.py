# 임시
x1, y1, r1, x2, y2, r2 = input().split()
x1 = int(x1)
y1 = int(y1)
r1 = int(r1)
x2 = int(x2)
y2 = int(y2)
r2 = int(r2)
z1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
z2 = r1 + r2
if z1 > z2 and z1 != 0:
    print("0")
elif z1 == z2 and z1 != 0:
    print("1")
elif z1 < z2 and z1 != 0:
    print("2")
elif z1 == 0 and r1 != r2:
    print("0")
else:
    print("-1")