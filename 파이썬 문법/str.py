string = "Python is the best choice"

# 문자열중 문자 b가 처음 나온 위치를 리턴, 만약 찾는 문자가 없을 시 -1리턴, int형으로 리턴함
print(string.find("b"))

# 위에 find와 같지만 찾는 문자가 없을 시 오류 리턴
print(string.index("b"))

# 문자열의 각각의 문자 사이에 탭을 삽입
print("   ".join(string))

# 문자열의 문자 개수를 int형으로 리턴
print(string.count("b"))

# 문자열 안에 특정한 값을 다른 값으로 바꾸어 준다
print(string.replace("Python", "C"))

# 문자열을 특정한 값을 기준으로 나누어 리스트 형으로 리턴
print(string.split())