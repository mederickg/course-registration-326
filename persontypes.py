class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    
   def __init__(self,year):
       super.__init__(self)
       self.year=year 
       
class Instructor(Person):
    #courses - list of courses they teach
    def __init__(self,courses):
        super.__init__(self)
        self.courses=courses
               

        
        