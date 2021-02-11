import re
p = re.compile('[a-z]+')
m = p.search("python")
if m:
    print("Match found: ", m.group())
else:
    print("No match")