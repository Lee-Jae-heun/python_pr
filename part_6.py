def std_weight(height, gender):
    if gender == "male":
        return height * height * 22
    elif gender == "female":
        return height * height * 21

gender = "male"
height = 175
# weight = round(std_weight(height/100, gender), 2)
print("키 %dcm %s의 표준 체중은 %.2fkg 입니다." % (height, gender, round(std_weight(height/100, gender), 2)))
