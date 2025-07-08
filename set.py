#Set():
#creating an empty set:
# a=set()
# print(type(a))

# set1={1,6,4,'abc'}
# print(type(set1))

#using Set()method
# days=set(["Monday","Tuesday","Wednesday","Thursday"])
# print(days)
# print(type(days))
# for i in days:
#     print(i)

#using add method:
# Months=set(["January","February","March","April","May","June"])
# print(Months)
# Months.add("July")
# print(Months)

#using update ()function:
# Months=set(["January","February","March","April","May","June"])
# print(Months)
# Months.update(["July","August"])
# print(Months)


#using Discard() method:
# months=set(["january","febuary","march"])
# print(months)
# months.discard("january")
# print(months)

#using remove () method:
# months=set(["january","febuary","march","april"])
# print(months)
# months.remove("january")
# print(months)

#SET OPERATIONS:
#Union:
# Days1={"Monday","Tuesday","Wednesday","Thrusday"}
# Days2={"Friday","Saturday","Sunday"}
# print(Days1|Days2)

#Intersection:
# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Monday","Tuesday","Sunday","Friday"}
# print(Days1&Days2)

#Set Comparisions:
# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Monday","Tuesday"}
# Days3={"Monday","Tuesday","Friday"}

#print(Days1>Days2)

#print(Days1<Days2)

#print(Days2==Days3)

#program1:
# list=["january","April","March","May","March","May"]
# a=set(list)
# print(a)

#program2:
# b=set()
# for i in range(5):
  
#      a=int(input("Enter the numbers:"))
#      b.add(a)
# print(b)

#program3:
# sentence=input("Enter a sentence:")
# found_vowels=set("aeiou")& set (sentence.lower())
# print(found_vowels)

# vowels=set()
# a=input("Enter a sentence:")
# for i in a.lower():
#     if i in 'aeiou':
#         vowels.add(i)
# print(vowels)       

#program4:
# words=["apple","orange","grapes","kiwi","dog","beach"]
# for word in words:
#     if len(set(word)) == len(word):
#         print(word)







    




