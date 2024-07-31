#Instance variable declare through constructor
class Student:
    def __init__(self,name,age):
        self.n1=name
        self.n2=age
    def display(self):
        print("Name=",self.n1)
        print("Age=",self.n2) #access value using self in another function
obj1=Student('Akansha',22)
obj1.display()
obj2=Student('aastha',21)
obj2.display()
print(obj1.n1) #access value through obj without using self
print(obj1.n2)
#---------------------------------
#through object---
class Student:
    
    def display(self):
        print("Name=",self.n1)
        print("Age=",self.n2) #access value using self in another function
obj1=Student()

obj1.n1="Akansha"
obj1.n2=22
obj1.display()
#----------------------------------
#through instance method-
class Student:
    def display(self,name,age):
        self.n1=name
        self.n2=age
    def show(self):
        print(self.n1,self.n2)
obj=Student()
obj.display('Akansha',22)
obj.show()
print(obj.n1,obj.n2)
#--------------------------------
# Static variable----
class Student:
    school="NEW ST MARY" #outside of method
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.center_code=101 #inside of constructor
    def display(self):
        Student.grade="10th" #instance of method
        print('Name=',self.name)
        print('Roll_no=',self.roll)
        print('School=',Student.school)
        print('Center=',Student.center_code)
        print('Grade=',Student.grade)
        print('City=',Student.city)
obj=Student('Akansha',101)
# obj.display()
print("school",Student.school)
print("school",obj.school)
Student.city='indore'#static variable declare outside of the class
obj.display()
print(Student.city)