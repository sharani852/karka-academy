#1
a=int(input("Enter a number:"))
if(a>=0):
    print("a is positive")
else:
    print("a is negative") 

#2
n=int(input("Enter a number:"))
if(n%2==0):
    print("Even number")
else:
    print("Odd number")

#3
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=a**b
print(c)

#4
a=float(input("Enter the first number:"))
b=float(input("Enter a second number:"))
if(a>b):
    print("a is greater")
else:
    print("b is greater")

#5
a=int(input("Enter a number:"))
if(a%4==0 and a%100!=0)or(a%400==0):
    print("Leap year")
else:
    print("Not a leap year")    


#6
mark=int(input("Enter the marks:"))
if(mark<60):
    print("Grade F")
elif(mark>=60 and mark<70):
    print("Grade D")
elif(mark>=70 and mark<80):
    print("Grade C")
elif(mark>=80 and mark<90):
    print("Grade B")
else:
    print("Grade A")

#7
age=int(input("Enter the age:"))
if(age<16):
    print("You cant drive")
elif(age>=16 and age<17):
    print("You can drive but not vote")
elif(age>=18 and age<24):
    print("You can vote but not rent a car")
else:
    print("You can do pretty much anything")  


8
for i in range(1,100):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz") 
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)    

#9
a=int(input("Enter a number:"))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(a," is a leap year")
else:
    print(a," is not a leap year")    
    










   






        

  
