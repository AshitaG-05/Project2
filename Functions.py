# To understand DEF Function

#1. With parameters
'''
def area(s):
    s=s**2
    print('Area of Square: ',s)
area(4) 


#2. Without parameters 


def area():
    s=int(input('Enter Side: ')) 
    s=s**2
    print('Area of the square: ',s)

area() '''

#to find area of triangle,square and rectangle
'''
def area(name):
    name=name.lower()
    if (name =='rectangle'): 
        l=int(input('Enter the length of the rectangle: '))
        b=int(input('Enter the breath of the rectangle: '))
        a1=l*b
        print('Area of the Rectangle: ',a1)
    elif(name=='square'):
        s=int(input('Enter the side of the Square: '))
        a2=s**2
        print('Area of Square: ',a2)
    elif(name=='triangle'):
        bs=int(input('Enter the base of the triangle: '))
        h=int(input('Enter the height of the triangle: '))
        a3=0.5*bs*h
        print('Area of the Triangle: ',a3)
    else:
        print('Sorry! No other Shape available')
        
print('Calculating Area of Shapes')
name=input('Enter the shape: ')

area(name) ''' 
 
        
        
#Construction of a Simple Calculator

def calc(num,a,b):
    if(num==1):
        print('ADDITON')
        sum=a+b
        print('Additon of the A and B is: ',sum)
    elif(num==2):
        print('SUBTRACTION')
        sub=a-b
        print('Substraction of the two numbers: ',sub)
        if(b>a): 
            print('Its a Negative number')
        else:
            print('Its a positive number')
    elif(num==3):
        print('MULTIPLICATION')
        mul=a*b
        print('Multiplication of the A and B is: ',mul)
    elif(num==4):
        print('DIVISION')
        div=a/b  
        print('Division of the A and B is: ',div)
    else:
        print('Sorry! Input values are wrong') 

print('CALCULATOR')
print('1. ADDITION')
print('2. SUBSTRACTION')
print('3. MULTIPLICATION')
print('4. DIVISION')
num=int(input('Please enter your choice= '))
a=int(input('Enter number A: '))
b=int(input('Enter number B: ')) 

calc(num,a,b)


#map and filter funtions 


def times2(var):
    return var*2

    

seq=[1,2,3,4,5]
list(map(times2,seq))

        
        
        
        
        
        
        
        
        
         
        
        
        
        
        
        
        