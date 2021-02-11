# int형 변수를 100을 더한 변수로 변환
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 문자열을 문자열의 길이로 변환
students = ["Kim", "Hong"]
students = [len(i) for i in students]
print(students)

# 문자열의 문자들을 대문자로 변환
students = ["Kim", "Hong"]
students = [i.upper() for i in students]
print(students)