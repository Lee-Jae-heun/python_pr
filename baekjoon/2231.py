import sys
N = str(sys.stdin.readline().rstrip())
Max = (len(N)-1)*9 + int(N[0])
num = int(N) - Max
Min = 9999999
N_sum = 0
for i in range(num, int(N)):
    Sum = 0
    i = str(i)
    for j in range(len(i)):
        Sum += int(i[j])
    i = int(i)
    Sum += i
    if Sum == int(N) and Min > Sum:
        Min = Sum
        N_sum = i
if N_sum:
    print(N_sum)
else:
    print(0)