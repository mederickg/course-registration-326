class School:
    
    def __init__(self,students,courses,faculty):
        self.students= students
        self.courses= courses
        self.faculty=faculty
    
    def add_course():
        """adds a course to the school.
        
        maybe we use the argparser here"""
        pass
        
    def addStudents(filepath):
        """Reads in a formatted file of students, constructs them, and adds them to the students at the school
        
        regex + reading in  from file"""
        pass
        
        #with open(filepath,'r',encoding='utf-8') as file:
        #    for line in file:
        
    def print_transcript(Student= None):
        """"""
        pass
    
    if __name__ == "__main__":
        
        pass
        
    def student_stats(year):
        """Not sure here, idea is maybe some way of demonstrating different gpa in a graph or something from students
        
        
        maybe gets gpa breakdown for all students in a certain class
        
        interesting spot for list comprehensions maybe"""
        pass
    def class_rankings():
        """prints the 5 highest ranked students in the class, based on gpa, returns sorted list of the students based on gpa,descending"""
        
class Course:
    
    def __init__(self, courseName,sections,prereqs):
        self.courseName=courseName
        self.sections= sections
        self.prereqs = prereqs
        
class Section:
    
    def __init__(self,instructor,time):
        self.instructor= instructor
        self.time = time
        
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
               

        
        