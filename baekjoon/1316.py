import sys
N = int(sys.stdin.readline().rstrip())
cnt_ = 0
for _ in range(N):
    word = str(sys.stdin.readline().rstrip())
    str_word = []
    cnt = 0
    for i in range(len(word)):
        if i == 0:
            str_word.append(word[i])
        else:
            if word[i-1] == word[i]:
                pass
            elif word[i] in str_word:
                cnt += 1
            else:
                str_word.append(word[i])
    if cnt == 0:
        cnt_ += 1
print(cnt_)