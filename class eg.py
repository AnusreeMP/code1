# class Student:
#  def __init__(self,name,id,age):
#     self.name=name
#     self.id=id
#     self.age=age

# s=Student("John",101,22)
# print(getattr(s,'name'))
# setattr(s,"age",23)
# print(getattr(s,'age'))
# print(hasattr(s,'id'))
# delattr(s,'age')
# print(s.age)

#INHERITANCE

#1.Single Inheritance:
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")        
# d=Dog()
# d.bark()
# d.speak()        

#2.Multilevel Inheritance:
# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking") 
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...") 
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()


#3.MULTIPLE INHERITANCE:
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b            
# class Calculation2:
#     def Multliplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.Summation(10,20))
# print(d.Multliplication(10,20)) 
# print(d.Divide(10,20)) 

#4.Hierarchical Inheritance:
# class Parent:
#     def func1(self):
#         print("This function in parent class.") 
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.") 
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
# object1=Child1()
# object2=Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


#POLYMORPHISM:
class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    def getroi(self):
        return 7
class ICICI(Bank):
    def getroi(self):
        return 8        
b1=Bank()
b2=SBI()
b3=ICICI()
print("Bank Rate if interest:",b1.getroi())
print("SBI Rate if interest:",b2.getroi())
print("ICICI Rate if interest:",b3.getroi())
