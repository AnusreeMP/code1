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
# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7
# class ICICI(Bank):
#     def getroi(self):
#         return 8        
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank Rate if interest:",b1.getroi())
# print("SBI Rate if interest:",b2.getroi())
# print("ICICI Rate if interest:",b3.getroi())

#example 2:
# class Bird:
    # def intro(self):
    #     print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.") 
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.") 
# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")
# obj_bird=Bird()
# obj_spr=sparrow()
# obj_ost=ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_spr.intro()
# obj_spr.flight()
# obj_ost.intro()
# obj_ost.flight()    

#Encapsulation:
#Protected members:
# class Base:
#     def __init__(self):
#         self._a=2
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class:",self._a)
#         self._a=3
#         print("Calling modified protected members outside class:",self._a)
# obj=Derived()

# obj2=Base()
# print("Acessing protected member of obj1:",obj._a)
# print("Acessing protected members of obj2:",obj2._a)

#2 Private members:
# class Base:
#     def __init__(self):
#         self.a="Hello"
#         self.__c="World"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling private member of base class:") 
#         print(self.__c)
# obj1=Base()
# print(obj1.c)
# obj2=Derived()

#Data Abstraction:
from abc import ABC
class Animal(ABC):
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return"Woof!"
class cat(Animal):
    def make_sound(self):
        return"Meow!"
dog=Dog()
cat=cat()
print(dog.make_sound())
print(cat.make_sound())        



