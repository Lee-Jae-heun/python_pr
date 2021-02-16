import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, S = map(str, sys.stdin.readline().rstrip().split())
    R = int(R)
    for i in range(len(S)):
        print(S[i]*R, end="")
    print("")