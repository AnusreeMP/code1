#RIGHT Half Pyramid: 
#n=5
#a=1
#for i in range(0,n):
 #   for j in range(0,i+1):
       #print("* ",end=" ")
       #a=a+1
    #print()

#LEFT Half Pyramid: 
#n=5
#for i in range(0,n):
 # for j in range(0,n-i):
  #    print(" ",end=" ")


  #for k in range(0,i+1):
   #   print("*",end=" ")  
  #print()


#Fully Pyramid
#n=5
#for i in range(0,n):
 #   for j in range(0,n-i):
  #      print("",end=" ")
#
 #   for k in range(0,i+1):
  #       print("*",end=" ") 
   # print() 

#INVERTED Right Half Pyramid
# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" ")  
#         a=a+1
#     print()  

#INVERTED Left Half Pyramid
#n=5
#a=1
#for i in range (n):
 #   for j in range(i):
  #    print(" ",end=" ")
    
   # for k in range(n-i):
    #  print("*",end=" ")
     # a=a+1
    #print()

#TNVERTED Full Pyramid:
#n=5
#=1
#for i in range(n):
 #   for j in range(i):
  #    print(" ",end="")

   # for k in range(n-i):
    #  print("* ",end="")  
     # a+=1
    # print()

#RHOMBUS Pattern 
#n=6
#for i in range(0,n):
 #  for j in range(0,i):
  #    print(" ",end="")

  # for k in range(4):
   #    print("*",end=" ") 
  # print()

#DIAMOND Pattern
n=5
for i in range(0,n-1):
  for j in range(0,n-i):
    print("",end=" ")

  for k in range(0,i+1):
     print("*",end=" ")
  print()
n=5

for i in range(n):
  for j in range(i+1):
      print(" ",end="")  
  for k in range(n-i):
      print("* ",end="")  
  print()


