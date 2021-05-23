mystr = input('Please input String :')

# for i in mystr:
#     if i==' ':
#         print('*')
#     else:
#         print(i)
    
print("what do you want")
print(' 1.lenght')
print(' 2.count of word')
print(' 3.split by word')  

myask = input('Pls Enter You Choice')
spl = mystr.split()
if myask == '1':
     print(len(mystr))
elif myask == '2':
    print(len(spl))
elif myask == '3':
    print(spl)

else:
    print("incorrect input")




