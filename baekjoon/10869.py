a, b = input().split()
a = int(a)
b = int(b)
if 1 <= a and b <= 10000:
    print("{}".format(a+b))
    print("{}".format(a-b))
    print("{}".format(a*b))
    print("{}".format(a//b))
    print("{}".format(a%b))