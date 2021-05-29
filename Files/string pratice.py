mystr = input('Please input Sentence :')

spl2 = mystr.split()
def point6():
    # global mystr
    if spl2==' ':
        print('*')
        # ret = ret + "*"

    else:
        print(mystr)

    
    # print("kk") 
    
print("What Do You Want?")
print(' 1.Lenght')
print(' 2.Count of Word')
print(' 3.Split by Word')
print(' 4.LowerCase')
print(' 5.UpperCase')  

myask = input('Pls Enter You Choice')
spl = mystr.split()
if myask == '1':
     print(len(mystr))
elif myask == '2':
    print(len(spl))
elif myask == '3':
    for x in spl:
        print(x)
elif myask == '4':
    print(mystr.lower())
elif myask == '5':
    print(mystr.upper())
elif myask == '6':
        point6()






         
          
    

else:
    print("incorrect input")

print(spl2)

input1 = input('Do You Want To Do Again?')

print(spl2)
