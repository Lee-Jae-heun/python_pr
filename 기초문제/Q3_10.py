import os
os.chdir("C:\\doit")
result = os.popen("dir")
print(result.read())