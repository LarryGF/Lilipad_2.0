import re
##MEMORY
##SIZE
file=open('asignacion.txt')
text = file.read()
patt1 = re.compile('VCPU=.+')
patt2 = re.compile('MEMORY=.+')
patt3 = re.compile(r'\s+(SIZE=.+")')
s = patt1.search(text)
s1 = patt2.search(text)
s2 = patt3.search(text)
print(s.group(),s1.group(),s2.group(1),sep='\n')
