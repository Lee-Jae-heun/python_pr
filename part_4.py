import random

user = range(1,21)
user = list(user)

random.shuffle(user)   # 리스트 값의 위치를 무작위로 바꿈

user = random.sample(user, 4)  # 리스트 중에 n개를 무작위로 골라 리스트로 리턴

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 :", user[:1])
print("커피 당첨자 :", user[1:])
print(" -- 축하합니다 -- ")