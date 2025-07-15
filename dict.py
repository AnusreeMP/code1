#Dict:
#create dict in python:
# captial_city={"Nepal":"Kathmandu","Italy":"Rome"}
# print(captial_city)
# for i in captial_city:
#     print( captial_city[i])

#Add element to a dict:
# captial_city={"Nepal":"Kathmandu","Italy":"Rome"}
# print("Initial Dictionary:",captial_city)
# captial_city["Nepal"]="Kathmandu"
# print("Updated Dictionary:",captial_city)

#change value of Dict:
# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print("Initial Dictionary:",student_id)
# student_id[112]="Stan"
# print("Updated Dictionary:",student_id)

#Acessing elements from dict:
# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print(student_id[111])
# print(student_id[113])

#Removing elements from dict:
# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# del student_id[111]
# print("Updated Dictionary",student_id)

#Iterating through a dict:
# squares={1:3,3:9,5:25,7:49,9:81}
# for i in squares:
#     print(squares[i])

#dict example:square of 1 to 10 numbers:
# a={}
# for i in range(1,11):
#   a[i]=(i*i)  
# print(a)

#zip example:
# keys=['name','age','city']
# values=['Alice',30,'New York']
# my_dict=dict(zip(keys,values))
# print(my_dict)
 
        #Functions:

#Function: example of user defined function:
# def square(num):
#     return num**2
# object_=square(6)  
# print("The square of the given number is:",object_)  
#another way:without return stmt:
# def square(num):
#     print (num**2)
# square(6)    


#example:
# def a_function(string):
#     return len(string)
# print(a_function("Functions")) 
# print(a_function("Python"))   

#Function Calling:
#1.with argument with return type:
#to find square:
# def square(num):
#     return num*num
# result=square(5)
# print("Square:",result) 

#2.with argument without return type:
#to print a greet msg:
# def greet(name):
#     print("Hello",name + "!")
# greet("Anu")    

#3.without argument with return type:
#function that returns a welcome message:
# def get_message():
#     return"Welcome to python programming!"
# msg=get_message()
# print(msg)

#4.without argument without return type:
#function to print numbers from 1 to 5:
# def print_numbers():
#     for i in range(1,6):   
#         print(i)
# print_numbers()   

#Function Arguments:1.(Default arguments)
# def function(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
 # Calling the function and passing only one argument:
# print("Passing only one argument")    
# function(30)

# 2.Keyword Arguments:
# def function(n1,n2=20):
#    print("number 1 is:",n1)
#    print("number 2 is:",n2)
# print("Without using keyword")
# function(n1=50,n2=30)

# def is_even(num):
#    if num%2==0:
#        print(num,"is even")
#    else:
#        print(num,"is odd")  

# a=int(input("Enter the number:")) 
# is_even(a)       


#Function example: with factorial
# def Factorial(num):
#    fact=1
#    for i in range(1,num+1):
#       fact=fact*i
#    return fact

# n=int(input("Enter a number:"))
# f=Factorial(n)
# print(f"Factorial of {n} is {f}")


#Function example 2:with leap year
# def is_leap_year(year):
#    if(year%4==0 & year%100!=0) or (year% 400==0):
#       return True
#    else:
#       return False

# year=int(input("Enter a year:"))
# if is_leap_year(year):
#    print("It is a leap year")
# else:
#    print("It's not a leap year")  


#simply displaying :
# def Display(name,age):
#     print(f"My name is {name} Iam {age} years old")

# Display(name="Ebin",age=27)  

#with **a print as dict:
# def Display(**a):
#   # print(a)
#   print(f"Hi {a['name']} Welcome to{a['course']} course")

# Display(name="Ebin",course="Python")  

def ADDITION(x,y):
   ans=x+y
   print(ans)

def SUBTRACTION(x,y):
   ans=x-y
   print(ans)

def MULTIPLICATION(x,y):
    ans=x*y
    print(ans)

def DIVISION(x,y):
     ans=x/y
     print(ans)
while True:
    print("1 .ADDITION")
    print("2 .SUBTRACTION")
    print("3 .MULTIPLICATION")
    print("4 .DIVISION")
    print("5.EXIT")
    choice = int(input("Enter your choice:"))
    if choice ==1:
      a=int(input("enter the first number:"))  
      b=int(input("enter the second number:"))
      ADDITION(a,b)
    elif choice ==2:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        SUBTRACTION(a,b)
    elif choice ==3:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        MULTIPLICATION(a,b)
    elif choice==4:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        DIVISION(a,b)
    elif choice==5:
        break


