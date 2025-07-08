#1
for i in range(1,11):
    print(i)

#2
for i in range(1,21):
    if(i%2==0):
        print(i)

#3
for i in range(1,21):
    if(i%2!=0):
        print(i)

#4
n=int(input("Enter a number:"))
f=1
for i in range(1,n+1):
    f*=i
print("The factorial is",f)    

#5
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)    

6
l = [10, 20, 30]
total = 0
for i in l:
    total += i
avg = total / len(l)
print("Average:", avg)

7
for i in range(1,6):
    print('*'*i)


#8
for i in range(1,6):
    print(i)

#9
for i in range(1,11):
    print(i)

#10
a=[10,20,30,40,10]
if(a[0]==a[4]):
    print("True")
else:
    print("False")    

#11
a=[10,20,30,43,50]
for i in a:
    if(i%5==0):
     print(i)


#12
ch=input("Enter a char:").lower()
if ch in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Consonant")    

#13
e=o=0
for i in range(10,56):
    if i%2==0: e+=1
    else: o+=1
print("Even:",e,"Odd:",o)

#14
for i in range(1,26):
    if i%5!=0: print(i)

#15
l=[3,4,5]
for n in l:
    f=1
    for i in range(1,n+1): f*=i
    print(f)

#16
a,b=30,20
if a*b<=500:
    print(a*b)
else:
    print(a+b)    

#17
a,b=15,25
print(max(a,b))

#18
a,b,c=12,25,19
print(max(a,b,c))


#19
x=[23,4,-6,23,-9,21,3,-45,-8]
p=[i for i in x if i>=0]
n=[i for i in x if i<0]
print("Positive:",p,"\nNegative:",n)

   
    

