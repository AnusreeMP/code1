#Homework:

#Recursive function to print numbers from n to 1:

# def print_numbers(n):
#     if n == 0:
#         return 1
#     c
# print_numbers(3)

#Recursive function to calculate the sum of first n natural numbers:
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#        print(n)
#        return n+sum(n-1)
# print(sum(3))

#Recursive function to find the sum of digits of number:
def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n//10)
 #print(sum(52))

#Recursive function to Reverse a string:
def rev(s):
    if len(s)==0:
        return s
    else:    
        return rev(s[1:])+s[0]
#print(rev("Java"))  



                        #Lambda functions

#To find the square of a number:
f=lambda a:a*a                      
print(type(f))
#print(f(3))

#To check if a number is even or odd :
even_odd=lambda x:"Even"if x%2==0 else"Odd"
# print(even_odd(5))
# print(even_odd(8))

#To find maximum of two numbers:
#max=lambda a,b,:a if a>b else b
#print("Maximum:",max(10,20))

# To check if a string starts with letter 'A' :
start_with_a=lambda s: s.lower().startswith('a')
print(start_with_a('Apple'))
print(start_with_a('apple'))


