url = "http://naver.com"
del_url = url.replace("http://", "")
del_url = del_url[:del_url.index(".")]
password = del_url[:3] + str(len(del_url)) + str(del_url.count("e")) + "!" 

print("생성된 패스워드 : %s" % password)