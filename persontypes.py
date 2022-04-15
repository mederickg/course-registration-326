class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Student(Person):
    
    def __init__(self,year,schedule):
       super.__init__(self)
       self.year=year
        
    def add_class():
        """adds a class to a students schedule if their schedule allows for it AND they meet prerequisites"""
        pass
    def drop_class():
        """drops a class, updates the student schedule as needed"""
        pass
        
            
        
       
class Instructor(Person):
    #courses - list of courses they teach
    
    def __init__(self,courses):
        super.__init__(self)
        self.courses=courses
        
    def give_grade():
        """
        Method takes a given student, and assigns them a final grade for a course
        
        Side Effects: impacts the students gpa calculation
        """
        pass
               

        
        