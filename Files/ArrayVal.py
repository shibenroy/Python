from array import *

Arr = array('i',[])

ArrInput = int(input('length of array'))

for i in range(ArrInput):
     ArrVal = int(input('Valur Of Array'))
     Arr.append(ArrVal)
print(Arr)     
