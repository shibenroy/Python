'''
Creater By: Shiben Roy

'''
print('Loading Converter')

# Metre to Centimetre
# metre to kilometre
# Area Finder
# Perimeter finder
def mtc():
    Metre = input('Pls inter Your Metre')
    Mc = int(Metre)
    mc1 = 100
    mct = Mc* mc1
    print(mct)

def mtk():
    kilo = input('Pls Input Your Kilo')
    mk = int(kilo)
    mk1 = 1000
    mkt = mk / mk1
    print(mkt)

def factor(x):
    Rim = []
    y = int(x)
    print('Factor of',y,'is' )
    for i in range(1, y):
        if y%i == 0 :
            Rim.append(i)
            print(i)

def areafind1():
    print('Please inter length and breadth')
    lenght1 = input("lenth")
    breadth1 = input('Breadth')
    intlen = int(lenght1)
    intbreadth = int(breadth1)
    lbtotal = intlen * intbreadth
    print(lbtotal)

def perimeterfind1():
    print('please inter length and breadth')
    length2 = input('pleas inter length')
    breadth2 = input('please input breadth')
    len2 = int(length2)
    beat2 = int(breadth2)
    lb2 = len2 + beat2
    lbx = lb2  + lb2
    print(lbx)
    

while True:
   
    print('What do you want')
    print('Metre to Centimetre (mtc) ')
    print('metre to kilometre (mtk) ')
    print('Factor')
    print('Find Area(AF)')
    print("Find Perimeter(FP)")

    print('')

    factorNum = input('Pls input choice >  ')

        
    myask1 = ''


    if factorNum == 'mtc':
        mtc()
    elif factorNum == 'mtk':
        mtk()
    elif factorNum == 'AF':
        areafind1() 
    elif factorNum == 'FP':
        perimeterfind1()       
    else:
        print('Wrong Input')


    print('input q to quit and c to countinue ')    

    while(countinue != 'q' and countinue != 'c' ):
        countinue = input('hi')
        if countinue == 'q':
            exit()
        elif countinue =='c':
            countinue    

    




