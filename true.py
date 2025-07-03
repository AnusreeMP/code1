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

#pop example:
# x=[]
# while True:
#   print("1.ADD")
#   print("2.REMOVE")
#   choice=int(input("Enter your choice:"))
#   if choice==1:
#     a=int(input("Enter a number:"))
#     x.append(a)
#     print(x)
    
#   elif choice==2:
#     b=int(input("Enter a value you want to remove:"))  
#     for i in range(len(x)):
#       if i<=len(x)-1:
#         if x[i]==b:
#          x.pop(i) 
#          print(x)


#del():used for removing one or more items from a list
# languages=['Python','Swift','C++','C','Java','Rust','R']
# del languages[1]
# print(languages) 
# del languages[-1] 
# print(languages) 
# del languages[0:2] 
# print(languages)   


#Remove()
# languages=['Python','Swift','C++','C','Java','Rust','R']
# languages.remove('Python')
# print(languages)

#reverse():
# prime_numbers=[2,3,5,7]
# prime_numbers.reverse()
# print('Reversed List:',prime_numbers)


#Repetition:
# list1=[12,14,16,18,20] 
# print(list1 * 2)

#Concatenation:
# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# print(list1+list2)


#length:
# list1=[12,14,16,18,19,23,17,30]
# print (len(list1))


#Iteration:
# list=[12,14,15,16,17]
# for i in list:
#   print(i)

# list2=['jonn','david','sam','alen']
# for i in list2:
#   print(i)

#Membership
# list1=[100,200,500,700]
# print(600 in list1)
# print(400 in list1)

#Max():
# list1=[103,675,897,200,543]
# print(max(list1))

# list2=['alen','sam',',dheiha','kiyaa']
# print(max(list2))


#Min()
# list1=[103,657,321,786,900]
# print(min(list1))


#Intersection()
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7] 
# #using intersection() method:
# intersection1=set(list1).intersection(list2)
# print(intersection1)

#using & operator:
# intersection2=set(list1)&set(list2)
# print(intersection2)

#example:
# a=[1,2,3,4,5]
# b=[3,4,5,6,7]
# c=[]
# for i in range(len(a)):
#   for j in range(len(b)):
#     if a[i]==b[j]:
#         c.append(b[j])
# print(c)

#Max and Min with loop:
# data=['david','alen','sam']
# b=data[0]
# c=data[0]
# for v in data[1:]:
#     if v > b:
#       b=v
#     if v < c:
#       c=v  
# print("maximum:",b)
# print("minimum:",c)

a=[100,300,675,897,245]
b=a[0]
c=a[0]
for v in a[1:]:
    if v > b:
      b=v
    if v < c:
      c=v  
print("maximum:",b)
print("minimum:",c)
