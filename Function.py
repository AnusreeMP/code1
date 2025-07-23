#Write a function that takes a list of numbers and return maximum:
def find_max(num):
    return max(num)
#print(find_max([2,8,6,9])) 


#Define a function that returns the reverse of a given string:
def reverse_string(s):
    return s[::-1]
# print(reverse_string("hello"))

#create a function that takes if a number is palindrome:
def is_palindrome(num):
    return str(num)==str(num) [::-1] 
#print(is_palindrome(121))   


#function that takes a string and counts the number of vowels:
def count(s):
    vowels=('aeiou')
    return sum(1 for char in s.lower() if char in vowels)
#print(count("hello python"))

#define a function that accepts a list and returns a new list with only even numbers:
#def list1(even):



#calculates the power of a number without using (** or pow):
def power(num):
    
    return num
print(power(6))   