N = int(input())
if 1 <= N <= 9:
    for i in range(1, 10): 
        print("{0} * {1} = {2}".format(N, i, N*i))