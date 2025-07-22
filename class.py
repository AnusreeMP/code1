#To create a object:
# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()   

#To delete  
# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display() 


#Example of object:
# class car:
#  def __init__(self,modelname,year):
#     self.modelname=modelname
#     self.year=year
#  def display(self):
#     print(self.modelname,self.year)
# c1=car("Toyota",2016) 
# c1.display()   

#Creating a constructor in python:
# class Employee:
#   def __init__(self,name,id):
#     self.id=id
#     self.name=name
#   def display(self):
#      print("ID:%d\n Name:%s"%(self.id,self.name))
# emp1=Employee("John",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

#Non parametersized constructor:
# class Student:
#     def __init__(self):
#       print("This is non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)  
# student=Student()
# student.show("John")        

     