me = {"tall":175, "weight":55}
print(me["tall"])
print(me["weight"])

# 딕셔너리의 새로운 값 추가 // 무조건 key값으로 접근
me["love"] = "game"

# 딕셔너리의 값 삭제
del me["tall"]

# 딕셔너리의 key 들만 출력
print(me.keys())

# 딕셔너리의 value 들만 출력
print(me.values())

# 딕셔너리의 key 와 value 쌍으로 출력
print(me.items())

# 딕셔너리 삭제
me.clear()