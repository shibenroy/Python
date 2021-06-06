# create a funtion which take multipe inputs and print those multiple input with there lenth
# create a add funtion where user will input multiple number and return the value and print later

def item(*val):
     for i in val:
         print(i,type(i))

     

item('good','hi','bye','hfhfh','asdfhiasgh')
item(12,23,53,23.5)

num1 = input('Enter a number to add')
num2 = input('Enter another number to add')


def add(a,b):
    c = a + b
    return c

add(num1,num2)


     