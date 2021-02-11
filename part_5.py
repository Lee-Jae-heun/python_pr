import random

time = []
count = 0

for i in range(1, 51):
    time = random.randint(5, 50)

    if 5 <= time and time <= 15:
        print("[O] %d번째 손님 (소요시간 : %d )" % (i, time))
        count += 1
    else:
        print("[ ] %d번째 손님 (소요시간 : %d )" % (i, time))

print("총 탑승 승객 : %d분" % count)