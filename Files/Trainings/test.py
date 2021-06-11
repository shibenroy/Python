def factor(x):
    y = int(x)
    print('Factor of',y,'is' )
    y = int(x)
    for i in range(1, y + 1):
        if y%i == 0 :
            print(i)

factorNum = input('Pls input num')

factor(factorNum)


         
