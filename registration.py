import pandas as pd 
import re


class Course_db():
    
    def __init__(self, path):
        self.courses = pd.read_csv(path)
    
    def add_courses(self, path): 
        temp = pd.read_csv(path)
        self.courses = pd.concat([self.courses, temp])

import persontypes
class School:
    
    GPAS = {'A': 4.0,'B':3.0,'C':2.0,'D':1.0,}
    
    def __init__(self,students,courses,faculty):

        self.students= students
        self.courses= Course_db(courses)
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
       
       
        
class Student():
    
   def __init__(self, name, age, year, credits,course_db):
        self.name = name
        self.age = age
        self.year = year
        self.credits = credits
        self.grades = {}
        self.gpa = 0.00
        self.schedule = pd.DataFrame()
        self.course_db = course_db
     
   def add(self,prefix,course_num,section_num): 
       pfx_filt =  self.course_db["Prefix"] == prefix 
       course_num_filt = self.course_db["Course number"] == course_num 
       sec_num_filt = self.course_db["Section number"] == section_num
       combined_filter = pfx_filt & sec_num_filt & course_num_filt
       
       entry = self.course_db[combined_filter]
       
       if entry.loc[entry.index[0],"Credits needed"] > self.transcript.loc[0,"credits"]:
           return ValueError("Have not met credit requirements")
       else:
        self.schedule = pd.concat([self.schedule,entry])
        self.schedule = self.schedule.drop(columns=['Credits needed'])
       
   def drop(self,prefix,course_num):
         pfx_filt =  self.course_db["Prefix"] == prefix 
         course_num_filt = self.course_db["Course number"] == course_num 
         combined_filt = pfx_filt & course_num_filt
         
         entry = self.schedule[combined_filt]
         drop_val = entry.index[0]
         self.schedule = self.schedule.drop([drop_val], axis = 0)
    
   def verify_time():
        pass
    
   def print_schedule(self):
        return self.schedule.head()
    
   def sort_schedule():
        """takes schedule dataframe, sorts its values in a list form before recreating the dataframe in order chronologically"""
    