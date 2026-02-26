#Operators in python==

#(1)Arthmatic Operators
num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
print(num1+num2)  #4+5=9
print(num1-num2)  #4-5=-1
print(num1*num2)  #4x5=20
print(num1//num2) #4//5=0
print(num1/num2)  #4/5=0.8
print(num1%num2)
print(num1**num2) #4x4x4x4x4=1024

#(2)Even or Odd checking
number=int(input("Enter a number: "))
if number%2==0:
    print("Number is Even")
else:
    print("Number is odd")



#Logical Operators
#(1)Create Simple Login 
username=input("Enter your name")
Password=int(input("Enter your password: "))
if username=="admin" and Password==1234:
    print("Login Successful")
else:
    print("Invalid Credetial")

#(2) Temperature Checking
Temperature=int(input("Enter a Temperature"))
if Temperature>30 and Temperature<40:
    print("Hot")
else:
    print("Normal")

#(3)
x=5
y=10
z=15
print(x<y and y<z)
print(y>x and y>z)
print(x<y or x>y)
print(not(x>y))


#Relational/Comparision
age=int(input("Enter your age"))
if age>=1:
    print("Eligible for vote")
else:
    print("Not Eligible")

#Largest of two numbers
x=int(input("Enter a first number: "))
y=int(input("Enter a second number: "))
if x<y:
    print("Second number is greater")
elif x>y:
    print("First number is greater")
else:
    print("Bothnmbers are equal")



#(1)Boolean Operators
Password=input("Enter a password")
if not Password:
    print("Password cant be empty")
else:
    print('Accepted')


#(2)
value=input("Enter a something")
if value:
    print("Truthy")
else:
    print("Falsy")

Password=input("Enter a Password: ")
if not Password:
    print("Password can't be empty")
else:
    print("Accepted")


#Identity Operators
a=[1,2,3]
b=a
c=[1,2,3]
print(a==b)
print(a is b)
print(c==a)
print(a is c)


#Membership Operators
names=["Bhavana","Sanjana","Prathibha","Priyanka"]
user_input=input("Enter a name: ")
if user_input in names:
    print("Exists")

else:
    print("Not Exists")

#(2)Word Check
sentence="Python is Powerful"
user_input=input("Enter a name: ")
if user_input in sentence:
    print("Sentence is in user input")
else:
    print("Sentence is not in user input")
