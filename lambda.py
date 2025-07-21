#lambda pgm to add 2num:
# f=lambda a,b:a+b
# print(type(f))
# print(f(45,12))

#lambda using map with function:
#numbers=[45,23,5,6] 
# def Fun(num):
#     return num*2
#print(list(map(Fun,numbers))) 


# using lambda without function:
# print(list(map(lambda x:x*2,numbers)))

# Lambda Using Filter method:

#numbers=[23,5,2,12,4,100,8]
# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#print(list(filter( is_even,numbers)))

#without function :
#print(list(filter(lambda num:True if num%2==0 else False,numbers)))  

# lambda using reduce method  Factorial:
# from functools import reduce
# s=reduce(lambda a,b:a*b,range(1,6)) 
# print(s)

