mystr = input('Please input Sentence :')

# for i in mystr:
#     if i==' ':
#         print('*')
#     else:
#         print(i)
    
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
    

else:
    print("incorrect input")

input1 = input('Do You Want To Do Again?')

if input1 == 'yes':
    print(mystr)