import sys
Max = 0
for i in range(9):  
    a = int(sys.stdin.readline().rstrip())
    if 0 < a < 100:
        if Max < a:
            cnt = i+1
            Max = a
print(Max, cnt, sep="\n")
