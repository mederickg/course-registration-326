import pandas as pd 
import re
from argparse import ArgumentParser

class School:
    
    GPAS = {'A': 4.0,'B':3.0,'C':2.0,'D':1.0,}
    
    def __init__(self,students,courses,faculty):
        """initializes a School object

        Args:
            students (list): list of student objects in the school
            courses (DataFrame): a dataframe of availible courses and sections
            faculty (list): list of faculty members
        """
        self.students= students
        self.courses= pd.DataFrame(pd.read_csv(courses))
        self.faculty=faculty
    
    def add_course(self, course):
        """Adds a course section to the courses dataframe

        Args:
            course (DataFrame): a course section
        """
        self.courses.append(course)
        
    def regex_match(self, line):    
        """matches values in a txt file line to create a Student object

        Args:
            line (string): a string containing student name, age, year, and credits earned
        """
        pattern = r"^(\S+\s\S+), (\d+), (\d+), (\d+)$"
        searched = re.search(pattern, line)
        self.students.append(Student(searched.group(0), searched.group(1), searched.group(2), searched.group(3), self.courses))   
        
    def addMultipleStudents(self, path):
        """allows users to use a txt file containing multiple students, and add them in mass to the School.students list

        Args:
            path (string): a path to a txt file
        """
        with open(path,'r',encoding='utf-8') as file:
           for line in file:
               self.regex_match(line) 
        
    def addStudent(self, name, age, year, schedule={}):
        """Adds a single student to the School.students list

        Args:
            name (str): student full name
            age (int): student age
            year (int): year of graduation
            schedule (dict, optional): student schedule. Defaults to {}.
        """
        self.students.append(Student(name, age, year, schedule))
    
    def print_grades(self, Student= None):
        pass
    
    def student_stats(year):
        """Not sure here, idea is maybe some way of demonstrating different gpa in a graph or something from students
        maybe gets gpa breakdown for all students in a certain class
        interesting spot for list comprehensions maybe"""
        pass
    
    def class_rankings():
        """prints the 5 highest ranked students in the class, based on gpa, returns sorted list of the students based on gpa,descending"""
    
    def __str__(self):
        """prints the informal representaion of the School object
        """
        print(f"There are {self.students.len()} students and {self.faculty.len()} \
           faculty at this school. This school offers {len(self.courses)} courses.")
       
       
        
class Student():
    
   def __init__(self, name, age, year, credits, courses):
        self.name = name
        self.age = age
        self.year = year
        self.credits = credits
        self.grades = {}
        self.gpa = 0.00
        self.schedule = pd.DataFrame()
        self.course_db = pd.read_csv(courses)
     
   def add(self,prefix,course_num,section_num): 
       pfx_filt =  self.course_db["Prefix"] == prefix 
       course_num_filt = self.course_db["Course number"] == course_num 
       sec_num_filt = self.course_db["Section number"] == section_num
       combined_filter = pfx_filt & sec_num_filt & course_num_filt
       
       entry = self.course_db[combined_filter]
       
       if entry.loc[entry.index[0],"Credits needed"] > self.credits:
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
        return self.schedule
    
   def sort_schedule():
        """takes schedule dataframe, sorts its values in a list form before recreating the dataframe in order chronologically"""
        pass
    
   
if __name__ == "__main__":
       pass

   
           
