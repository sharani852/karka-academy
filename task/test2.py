#1
firstName="Sharu"
lastName="NL"
print(firstName)
print(lastName)
user_name="shar@gmail"
password_key="12345"
print(user_name)
print(password_key)

#2
a=10
b=30
c=a+b
print(c)

#3
import math
radius=float(input("Enter the radius:"))
area=math.pi*(radius**2)
print("Area of circle is:",area)

#4
l=float(input("Enter the length:"))
w=float(input("Enter the width:"))
area= l*w
print("Area of rectangle is:",area)

#5
b=float(input("Enter the base:"))
h=float(input("Enter the height:"))
area=(b*h)/2
print("Area pf triangle is",area)

#6
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=a+b
d=a-b
e=a*b
f=a/b
print("Addition:",c)
print("Subtraction:",d)
print("Multiplication",e)
print("Division",f)

#7
a=10
b=20
a=b
print(a)
a+=b
print(a)
b-=a
print(b)
a*=b
print(a)
b/=a
print(b)

#8
a=10
a+=20
print(a)
a=70
a-=10
print(a)

#9
a=10
b=20
print(a==b)
print(a<=20)
print(a>=80)
print(a<b)
print(b>80)
print(a!=b)

#10
a=10
b=20
print((a>b)and(10<=a))
print((a==b)or(a!=b))
print(not(a==2))

#11
#Using third variable
a=10
b=30
temp=a
a=b
b=temp
print("After swapping:a=",a,"b=",b)


#Without using third variable
a=10
b=30
a=a+b
b=a-b
a=a-b
print("After swapping:a=",a,"b=",b)

#12
a=10
b=20
c=30
d=(a+b+c)/3
print("Average of three numbers is",d)

#13
a=10
b=30
c=12
d=3
e=((a+b)*c)/d
print("The result is:",e)

#14
Tamil=float(input("Enter tamil mark:"))
English=float(input("Enter english mark:"))
Maths=float(input("Enter maths mark:"))
Science=float(input("Enter science mark:"))
Social=float(input("Enter social mark:"))
Total=Tamil+English+Maths+Science+Social
Average=(Total/5)
print("Total is:",Total)
print("Average is",Average)