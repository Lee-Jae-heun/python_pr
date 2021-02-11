subway = ["유재석", "조세호", "박명수"]

# 리스트에 있는 값의 위치를 리턴
print(subway.index("조세호"))

# 리스트의 마지막 자리에 값을 추가
subway.append("하하")

# 리스트에 값 삽입
subway.insert(1, "정형돈")

# 리스트의 가장 뒤에 있는 값을 삭제
subway.pop()

# 리스트에 같은 값을 가진 문자의 개수 리턴
subway.append("유재석")
subway.count("유재석")

# 리스트의 정렬
num_list = [2, 5, 3, 1, 4]
num_list.sort()

# 리스트 순서 뒤집기
num_list.reverse()

# 모두 지우기
num_list.clear()

# 다양한 자료형을 한 리스트에 입력가능
mix_list = ["유재석", 20, True]

# 다른 두 리스트를 합칠 수 있다
num_list.extend(mix_list)