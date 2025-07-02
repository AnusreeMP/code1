# while True:
#     print("1 .ADDITION")
#     print("2 .SUBTRACTION")
#     print("3 .MULTIPLICATION")
#     print("4 .DIVISION")
#     print("5.EXIT")
#     choice = int(input("Enter your choice:"))
#     if choice ==1:
#       a=int(input("enter the first number:"))  
#       b=int(input("enter the second number:"))
#       print(a+b) 
#     elif choice ==2:
#         a=int(input("enter the first number:"))
#         b=int(input("enter the second number:"))
#         print(a-b)
#     elif choice ==3:
#         a=int(input("enter the first number:"))
#         b=int(input("enter the second number:"))
#         print(a*b)
#     elif choice==4:
#         a=int(input("enter the first number:"))
#         b=int(input("enter the second number:"))
#         print(a/b)
#     elif choice==5:
#         break


# while True:
#     print("1.Registration")
#     print("2.Login")
#     print("3.Exit")
#     choice =int(input("enter the menu:"))
#     if choice==1:
#       a=input("enter the name:")
#       b=input("enter the age:")
#       if int (b) <= 18:
    #     print("you are not eligible")
    #     continue
    #   c=input("enter the address:")
    #   d=input("enter the phone number:")
    #   if len(d)==10:
    #     print("verified")
    #   else:
    #     print("Invalid")
    #     break 
    #   e=input("enter the username:")
    #   f=input("enter the password:") 
    # elif choice==2:
    #     g=input("enter the username:")
    #     h=input("enter the password:") 
    #     if g==e and h==f :
    #       print("Login sucessfully") 
    #       print("The Details")
    #       print("name :",a)
    #       print("age :",b)
    #       print("address :",c)
    #       print("phone number :",d)
    #       print("username :",e)
    #       print("password :",f)
    #     else:
    #       print("wrong username or password") 
    # elif choice==3:
    #     break           


#Indexing:
# message='PYTHON IS FUN'
# print(message.upper())


#count ()eg:
# txt="I love apples,apples are my favourite fruits"
# x=txt.count("p")
# print(x)


#find()
# message="Python is a fun programming language"
# print(message.find('fun'))

#replace()
# text='bat ball'
# replaced_text =text.replace('ba','ro')
# print(replaced_text)


#append
# numbers=[21,34,54,12]
# print("before Append:",numbers)
# numbers.append(32)
# print("after Append:",numbers)

#insert
# vowel=['a','e','i','u']
# vowel.insert(3,'o')
# print('List:',vowel)

#extend
# prime_numbers=[2,3,5]
# print("List:",prime_numbers)
# even_numbers=[4,6,8]
# print("List2:",even_numbers)
# prime_numbers.extend(even_numbers)
# print("List after append:",prime_numbers)

#example:
# a=[]
# n=int(input("Enter the range:"))
# for i in range(0,n):
#   if i%2==0:
#     a.append(i)
# print("list",a) 


#removing an item from a list:
# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('Removed Element:',removed_element)
# print('Updated List:',prime_numbers)


#remove odd numbers with pop element
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#   if i<=len(a)-1:
#     if a[i]%2!=0:
#       a.pop(i)
# print("List=",a)


x=[]
while True:
  print("1.ADD")
  print("2.REMOVE")
  choice=int(input("Enter your choice:"))
  if choice==1:
    a=int(input("Enter a number:"))
    x.append(a)
    print(x)
    
  elif choice==2:
    b=int(input("Enter a value you want to remove:"))  
    for i in range(len(x)):
      if i<=len(x)-1:
        if x[i]==b:
         x.pop(i) 
         print(x)
        

  
