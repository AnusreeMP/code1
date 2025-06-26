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
# n=4
# for i in range(0,n-1):
#   for j in range(0,n-i):
#     print("",end=" ")

#   for k in range(0,i+1):
#      print("*",end=" ")
#   print()
# n=4

# for i in range(n):
#   for j in range(i+1):
#       print(" ",end="")  
#   for k in range(n-i):
#       print("* ",end="")  
#   print()

#HOLLOW Square Pattern
# n=5
# for i in range(0,n):
#   for j in range(0,n):
#     if(i==0 or i==n-1 or j==0 or j==n-1):
#        print("*",end=" ")
#     else:
#         print(" ",end=" ")
#   print()  

#FLOYD'S Triangle:
# n=4
# a=1
# for i in range(n):
#   for j in range(i+1):
    
#     print(a,end=" ")
#     a+=1
#   print()

#HOURGLASS Pattern:
# n=5
# for i in range(n):
#   for j in range(i+1):
#     print(" ",end="")
#   for k in range(0,n-i):
#     print("* ",end="")
#   print() 

# n=5
# for i in range(0,n):
#   for j in range(0,n-i):
#     print("",end=" ")
#   for k in range(i+1):
#     print("*",end=" ")
#   print()  

#PASCAl'S Triangle Pattern:
# n=7
# for i in range(n):
#   print(" " * (n-i), end="")
#   num=1
#   for j in range(i+1):
#      print(num,end=" ")
#      num=num*(i-j)//(j+1)
#   print()   


# HOLLOW Full Pyramid:
n=5
for i in range(n):
  print(" " * (n-i-1),end=" ")
  for j in range(2*i+1):
      if j==0 or j==2*i or i==n-1:  
       print("*",end="") 
      else:
        print(" ",end="") 
  print() 

#HOLLOW Inverted Pyramid:
# n=5
# for i in range(n):
#    print(" "*i,end="")
#    for j in range(2*(n-i)-1):
#        if j==0 or j==(2*(n-i)-2) or i==0:
#            print("*",end="")
#        else:
#            print(" ",end="") 
#    print()  

#HOLLOW Diamond Pyramid:
# n=4
# for i in range(n):
#   print(" " * (n-i-1),end="")  
#   for j in range(2 * i + 1):
#     if j==0 or j==2 * i:
#       print("*",end="") 
#     else:
#       print(" ",end="") 
#   print()
# for i in range(n-2,-1,-1):
#   print(" " * (n-i-1),end="")  
#   for j in range(2*i+1):
#      if j==0 or j==2*i:
#         print("*",end="")
#      else:
#         print(" ",end="")  
#   print()         


# for i in range(65,70):
#   for j in range(65,70):
#     print(chr(j),end=" ")
#   print()