import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"이재흔", "나이":20, "취미":["게임", "코딩"]}
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 저장
print(profile)
profile_file.close()

################################################################

with open("profile.pickle", "w") as profile_file:
    profile_file = {"이름":"이재흔", "나이":20, "취미":["게임", "코딩"]}

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) #close 해줄 필요없음

