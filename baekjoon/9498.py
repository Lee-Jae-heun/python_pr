score = int(input())
# score = int(score)
if 0 <= score <= 100:
    if score >= 90:
        print("A")
    elif 80 <= score <= 89:
        print("B")
    elif 70 <= score <= 79:
        print("C")
    elif 60 <= score <= 69:
        print("D")
    else:
        print("F")