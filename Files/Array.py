import array 
vals = array('i',[5,9,8,4,2])

SqRoot = array(vals.typecode, (a*a for a in vals))

i = 0

while i<len(SqRoot):
    print(SqRoot[i])
    i+=1