data = """
부서 :
이름 :
업무 요약 :
"""

for i in range(1, 2):
    name = str(i) + "주차.txt"
    title = "- " + str(i) + " 주차 주간보고 -"
    with open(name, "w", encoding="utf8") as file_:
        file_.write(title + "\n" + data)