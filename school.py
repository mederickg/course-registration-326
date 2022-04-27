from persontypes import Student, Person, Instructor
import re

class School:
    
    def __init__(self,students,courses,faculty):

        self.students= students
        self.courses= courses
        self.faculty=faculty
    
    def add_course(self, course):
        """adds a course to the school.
        
        maybe we use the argparser here"""
        self.courses.append(course)
        
    def addMultipleStudents(self, path):
        """Reads in a formatted file of students, constructs them, and adds them to the students at the school
        
        regex + reading in  from file"""
        
        with open(path,'r',encoding='utf-8') as file:
               #re.search function to find student name, year, and ID
               #build Student objects for each line in the file
               #add student objects to self.students
           for line in file:
               pattern = r"^(\S+), (\S+), (\d+)$"
               searched = re.search(pattern, line)
               self.students.append(Student(searched.group(0), searched.group(1)))
               pass
           
    def addStudent(self, name, age, year, schedule={}):
        #at some point this function will be able to order the schedule 
        self.students.append(Student(name, age, year, schedule))
    
    def print_grades(self, Student= None):
        #looks at student grades in each class and prints it
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
        
        