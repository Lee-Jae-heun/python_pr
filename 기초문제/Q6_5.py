import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
tab_text = f.read()
f.close()

space_text = tab_text.replace("\t", " "*4)
f = open(dst, 'w')
f.write(space_text)
f.close()
