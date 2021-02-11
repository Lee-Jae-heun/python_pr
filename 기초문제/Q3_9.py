import sys
num = sys.argv[1:] #파일이름을 제외한 명령 행의 모든 값을 num에 입력

result = 0
for number in num:
    result += int(number)
print(result)