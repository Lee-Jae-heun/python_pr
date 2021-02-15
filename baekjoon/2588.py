a = input()
b = input()
a = int(a)
b1 = b[2]
b2 = b[1]
b3 = b[0]
b = int(b)
if 99 < a < 1000 and 99 < b < 1000:
    print("{}".format(a*int(b1)))
    print("{}".format(a*int(b2)))
    print("{}".format(a*int(b3)))
    print("{}".format(a*b))