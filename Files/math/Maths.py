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
    
factorNum = ''

   
print('What do you want')
print('Metre to Centimetre (mtc) ')
print('metre to kilometre (mtk) ')
print('Factor')
print('')

factorNum = input('Pls input choice')

    



if factorNum == 'mtc':
    mtc()

elif factorNum == 'mtk':

    mtk()
elif factorNum == 'areafind1':
    areafind1()    
else:
    print('Wrong Input')    





