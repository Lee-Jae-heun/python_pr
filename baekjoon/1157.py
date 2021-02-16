import sys
word = str(sys.stdin.readline().rstrip())
cnt = [0]*91
Max = 0
for i in range(len(word)):
    if ord(word[i]) > 96:
        cnt[ord(word[i])-32] += 1
    else:
        cnt[ord(word[i])] += 1
for i in range(65, 91):
    if Max < cnt[i]:
        Max = cnt[i]
        Max_c = i
    elif Max == cnt[i]:
        Max_c = 63
print(chr(Max_c))