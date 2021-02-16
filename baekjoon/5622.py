import sys
string = str(sys.stdin.readline().rstrip())
cnt = 0
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 67:
        cnt += 3
    elif 68 <= ord(string[i]) <= 70:
        cnt += 4
    elif 71 <= ord(string[i]) <= 73:
        cnt += 5
    elif 74 <= ord(string[i]) <= 76:
        cnt += 6
    elif 77 <= ord(string[i]) <= 79:
        cnt += 7
    elif 80 <= ord(string[i]) <= 83:
        cnt += 8
    elif 84 <= ord(string[i]) <= 86:
        cnt += 9
    elif 87 <= ord(string[i]) <= 90:
        cnt += 10
print(cnt)