# 방법 1 / C언어와 비슷한 문법
age = 20
print("나는 %d살입니다." % age)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살입니다." .format(age = 20))
print("나는 {color1}색과 {color2}색을 좋아해요." .format(color1 = "파란", color2 = "빨간"))

# 방법 4 / 파이썬 3.6버전이상 부터 지원
age = 20
color1 = "파란"
color2 = "빨간"
print(f"나는 {age}살입니다.")
print(f"나는 {color1}색과 {color2}색을 좋아해요.")

##############################################################
                        # 표준입출력 #

# sep="x" 값 사이에 x값을 삽입하여 출력, end="x" 출력의 마지막 부분에 x값 출력
print("Python", "Java", sep=",", end="?")

# sys.stdout 표준출력으로 처리, sys.stderr 표준에러로 처리, 사용하려면 sys임포트 해야함
import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# ljust 왼쪽에서 8칸 정렬, rjust 오른쪽에서 4칸 정렬
scores = {"수학" : 90, "영어" : 60, "코딩" : 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill(n) n번째자리까지 값을 채우되, 값이 없는 빈공간은 0으로 채운다 // 단 자료형은 str일것
for num in range(1, 21):
    print("대기번호 : %s" % str(num).zfill(3))

# 입력받은 값은 모두 str형으로 저장된다
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")

###################################################################
                        # 다양한 출력포맷 #

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하고 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어줌
print("{0:,}".format(1000000000))

# 3자리 마다 콤마를 찍고 +- 부호도 붙음
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

# 3자리 콤마, 부호, 자릿수 확보, 빈 자리 ^로 채움
print("{0:^<+30,}".format(1000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 / 소수점 3째자리에서 반올림 
print("{0:.2f}".format(5/3))