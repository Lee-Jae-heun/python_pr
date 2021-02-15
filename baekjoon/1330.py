a, b = input().split()
a = int(a)
b = int(b)
if -10000 <= a <= 10000 and -10000 <= b <= 10000:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    elif a == b:
        print("==")