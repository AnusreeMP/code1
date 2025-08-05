'''class father:
    def skill(self):
        print("farmming")

class mother:
    def hobby(self):
        print("pencil drawing")

class child (father,mother):
    pass


c=child()
c.skill()
c.hobby()'''


'''class grantparents:
    def old_skill(self):
        print("farming")

class parents(grantparents):
    def skill(self):
        print("teaching")

class child(parents):
    pass


ch=child()
ch.old_skill()
ch.skill()'''


'''class grandfather:
    def house(self):
        print("grandfather's house")

class father (grandfather):
    def car(self):
        print("father's car")

class son(father):
    def bike(self):
        print("sons's bike")             


s=son()


s.house()
s.car()
s.bike()
'''


'''class person:
    def __init__ (self,name):
        self.name = name
        print(f"[person] name set to:{self.name}")

class employee(person):
    def __init__ (self,name ,employee_id):
        super().__init__(name)
        self.employee_id=employee_id
        print(f"[employee] id set to:{self.employee_id}")

    def show_info(self):
     
        print(f"employee id:{self.employee_id}")


class manager(employee):
    def __init__ (self,name,employee_id,department):
        super().__init__(name,employee_id)
        self.department=department   
        print(f"departmrent:{self.department}")


    def show_info(self):
        super().show_info()
        print(f"departmemt:{self.department}")

m = manager("nithin",1024,"sales")

print("\n--- manager full info ---")
m.show_info()       
        '''

'''     
def Dec(fun):
    def wrapper(message):
        a=message.upper()


        fun(a)
    return wrapper            
        
@ Dec
def greetings(m):
    print(m)


greetings("hello develepors")
'''

'''
def subtraction (fun):
    def wrapper (a,b):
        if a<b:
             a,b=b,a

        return fun(a,b)
    return wrapper


@subtraction
def subtract(a,b):
    print(a-b)

subtract(3,7)
subtract(7,3)
subtract(7,7)

'''


# private and protect

#polymorphism
'''from abc import ABC,abstractmethod
class parents(ABC):
    @abstractmethod
    def fun(self):
        pass


class child(parents):
     def display(self):
        print("hi")
     def fun(self):
        print("abstract method implemetation")


ob=child()
ob.display()
ob.fun()
'''
        
        
        