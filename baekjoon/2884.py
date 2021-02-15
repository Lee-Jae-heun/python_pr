H, M = input().split()
H = int(H)
M = int(M)
if 0 <= H <= 23 and 0 <= M <= 59:
    M -= 45
    if M < 0:
        H -= 1
        M += 60
        if H < 0:
            H += 24
    print("{0} {1}".format(H, M))