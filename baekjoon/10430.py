a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if 2 <= a <= 10000 and 2 <= b <= 10000 and 2 <= c <= 10000:
    print("{}".format((a+b)%c))
    print("{}".format(((a%c)+(b%c))%c))
    print("{}".format((a*b)%c))
    print("{}".format(((a%c)*(b%c))%c))