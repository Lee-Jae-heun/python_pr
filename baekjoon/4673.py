bools = []
def self_num(num):
    num = str(num)
    total = 0
    for i in range(len(num)):
        total += int(num[i])
    total = int(num) + total
    return total

for i in range(1, 10001):
    bools.append(self_num(i))

bools.sort()
for i in range(1, 10000):
    if bools.count(i) == 0:
        print(i)