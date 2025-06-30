#1

def sayhello():
    print("Hello,World!")
sayhello()   

#2
def sum(a,b):
    c=a+b
    return c  
a=10
b=20
print(sum(a,b))

#3
def mul(a,b):
    c=a*b
    print(c) 
mul(9,6)   

#4
def mul(a,b):
    c=a*b
    return(c)
a=20
b=40
print(mul(a,b))

#5
def div(a,b):
    c=a/b
    return(c)
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(div(a,b))

#6
def fact(n):
    result=1
    for i in range(1,1+n):
        result*=i
    return result
print("Factorial of 5 is:",fact(5)) 


#7
def square(a):
    c=a**2
    return(c)
a=int(input("Enter a number:"))
print(square(a)) 




        

    
 
    

    