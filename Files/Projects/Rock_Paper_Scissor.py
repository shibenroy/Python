import random

userinput = ""
comp_input = ''



while (True):
    countinue1 = ''
    print(" Please enter [R]ock or  [P]aper or [S]cissor")
    userinput = input('User Input : ')
    userinput = userinput.capitalize()
    mylist = ['R','P','S']

    if userinput not in mylist:
        print('Incorrect Input, Please enter [R]ock or  [P]aper or [S]cissor   ...........')
    else:
        comp_input = random.choice(mylist)
        print(f"user input is {userinput} and Computer input is {comp_input}")

    print()
    print()

    # Paper
    if  userinput == 'P' and comp_input == 'R':
        print('User Win!!!')
    elif userinput == 'P' and comp_input == 'S':
        print('Computer Wins')
    elif userinput == 'P' and comp_input == 'P':
        print('Draw!!')
    # Rock       
    elif userinput == 'R' and comp_input == 'P':
        print('Computer Win!!!')
    elif userinput == 'R' and comp_input == 'R':
        print('Draw!!!')
    elif userinput == 'R' and comp_input == 'S':
        print('User Win !!!')      
    # Scissor  
    elif userinput == 'S' and comp_input == 'R':
        print('Computer Win !!!')
    elif userinput == 'S' and comp_input == 'S':
        print('Draw!!!')
    elif userinput == 'S' and comp_input == 'P':
        print('User Win !!!') 
    
    print()
    print('To Countinue Type - C -  And to Quit Type - Q - .......................')          
    
    while (countinue1 != 'Q' and countinue1 != 'C'):
        countinue1 = input()
        countinue1 = countinue1.capitalize()
        if countinue1 == 'Q': 
            exit()
        elif countinue1 == 'C':
            continue      
