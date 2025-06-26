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


while True:
    print("1.Registration")
    print("2.Login")
    print("3.Exit")
    choice =int(input("enter the menu:"))
    if choice==1:
      a=input("enter the name:")
      b=input("enter the age:")
      if int (b) <= 18:
        print("you are not eligible")
        continue
      c=input("enter the address:")
      d=input("enter the phone number:")
      if len(d)==10:
        print("verified")
      else:
        print("Invalid")
        break 
      e=input("enter the username:")
      f=input("enter the password:") 
    elif choice==2:
        g=input("enter the username:")
        h=input("enter the password:") 
        if g==e and h==f :
          print("Login sucessfully") 
          print("The Details")
          print("name :",a)
          print("age :",b)
          print("address :",c)
          print("phone number :",d)
          print("username :",e)
          print("password :",f)
        else:
          print("wrong username or password") 
    elif choice==3:
        break           