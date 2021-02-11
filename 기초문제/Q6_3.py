def getTotalPage(m, n):
    if m % m == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(30, 10))