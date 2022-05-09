import string
import pandas as pd 
import re
from argparse import ArgumentParser
import sys

class School:
    
    GPAS = {'A': 4.0,'B':3.0,'C':2.0,'D':1.0,}
    
    def __init__(self,courses):
        """initializes a School object

        Args:
            students (list): list of student objects in the school
            studentsdict (dict): Dictionary of student names as keys and student object as value
            courses (DataFrame): a dataframe of availible courses and sections
            faculty (list): list of faculty members
        """
        self.students= []
        self.studentsdict = {str:Student}
        self.courses= pd.DataFrame(pd.read_csv(courses))
    
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
        searched = re.search(pattern, line.strip())
        self.students.append(Student(searched.group(1), searched.group(2), searched.group(3), searched.group(4), self.courses))
        self.studentsdict[searched.group(1)] = Student(searched.group(1), searched.group(2), searched.group(3), searched.group(4), self.courses)   
        
    def addMultipleStudents(self, path):
        """allows users to use a txt file containing multiple students, and add them in mass to the School.students list

        Args:
            path (string): a path to a txt file
        """
        with open(path,'r',encoding='utf-8') as file:
           for line in file:
               self.regex_match(line)
           
    
    def print_grades(self, student= None):
        #looks at student grades in each class and prints it
        # student will be a string of the student name 
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
    
    def student_stats(self, course):
        """Graphs the GPA of all students that have the argument course in their
        schedule (overall GPA, not course GPA)"""
        zero, one, two, three, four = 0, 0, 0, 0, 0
        for student in self.students:
            gpa_lst = [student.gpa for i in student.schedule.index if 
             (student.schedule['Prefix'][i] + 
              student.schedule['Course number'][i] + 
              student.schedule['Section number'][i]) == course]
        
        for gpa in gpa_lst:
            str(gpa)
            dot = gpa.find('.')
            simple_gpa = int(gpa[dot - 1])
            if simple_gpa == 0:
                zero += 1
            elif simple_gpa == 1:
                one += 1
            elif simple_gpa == 2:
                two += 1
            elif simple_gpa == 3:
                three += 1
            else:
                four += 1
                
        df = pd.DataFrame({'GPA':['0.0', '1.0', '2.0', '3.0', '4.0'], 
                           'num_students':[zero, one, two, three, four]})
        df.plot.bar(x = 'GPA', y = 'num_students', rot = 0)
        ## Rn it only plots a bar graph, I could maybe have it return something
        ## that we can actually use. Lmk what u think.
                
    def class_rankings():
        """prints the 5 highest ranked students in the class, based on gpa, returns sorted list of the students based on gpa,descending"""
    
    def __str__(self):
        """prints the informal representaion of the School object
        """
        print(f"There are {self.students.len()} students and {self.faculty.len()} \
           faculty at this school. This school offers {len(self.courses)} courses.")
       
       
        
class Student():
    """Student class contains all student information for studnets held in the shchool, for use in 
        data aggregtion"""
    def __init__(self, name, age, year, credits, courses):
        self.name = name
        self.age = int(age)
        self.year = int(year)
        self.credits = int(credits)
        self.grades = {}
        self.gpa = 0.00
        self.schedule = pd.DataFrame()
        self.course_db = courses
     
    def add(self,prefix,course_num,section_num): 
       """Adds course to student schedule given they meet credit/time requirements"""
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
        """drops course from student schedule"""
        pfx_filt =  self.course_db["Prefix"] == prefix 
        course_num_filt = self.course_db["Course number"] == course_num 
        combined_filt = pfx_filt & course_num_filt
         
        entry = self.schedule[combined_filt]
        drop_val = entry.index[0]
        self.schedule = self.schedule.drop([drop_val], axis = 0)
    
    def verify_time():
        pass
    
    def print_schedule(self):   
        print(self.schedule.to_string())
    
    def sort_schedule():
        """takes schedule dataframe, sorts its values in a list form before recreating the dataframe in order chronologically"""
        pass
    
   
def parse_args(arglist):
    
    parser = ArgumentParser("get filepaths to initiate the school program")
    parser.add_argument("students", help="filepath to a file containing students enrolled in the school") 
    parser.add_argument("courses",help = "filepath to a file containing the courses held at the school")
    args = parser.parse_args(arglist)
    
    return args  
     
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    
    ##for now, specialized for the demo
    
    umd = School(args.courses)
    print(args.students)
    umd.addMultipleStudents(args.students)
    umd.studentsdict["Giannis Antetokounmpo"].add("INST", 335, 102)
    umd.studentsdict["Giannis Antetokounmpo"].add("INST",126,102)
    
    
    perspective = input("Hello, are you accessing from a student or school perspective? 1 for student, 2 for school: ") 

    if(perspective == '1'):

            name = input("Please enter your full name in format fname, lname: ")
            age = input("Please enter your age: ")
            year = input("Please enter your class (graduation year): ")
            credits = input("How many credits are you enrolling with?: ")
            user = Student(name,int(age),int(year),int(credits)) 
            umd.students.append(user)
            track = (umd.students.index(user))
            
            option = input("What would you like to do today? \n1.add class\n 2.drop class\n3.print transcript\n4.exit")

            while(option != 4):
                
                if(option == 1):
                    pass
                elif(option ==2):
                    pass
                elif(option == 3):
                    pass
                else:
                    option =input("please enter a valid option: \n 1.add class\n 2.drop class\n3.print transcript\n4.exit\n")
        
    else:
        option = input("What would you like to do today?\n1.add multiple students\n2.add single student\n3.add course \n4. print student transcript\n5. Exit ")
        
        while(option!='5'):
            
            
            
            if(option == '1'):
                choice = input("please enter a file path to students you would like to add")
                
                umd.addMultipleStudents(input)
                
                option =("complete! would you like to do anything else? \n 1.add multiple students\n2.add single student\n3.add course \n4. print student transcript\n5. Exit\n")
            elif(option == '2'):
                pass
            elif(option == '3'):
                pass
            elif(option == '4'):
                choice  = input("Please enter the student: ")
                
                umd.studentsdict[choice].print_schedule()
                option = input("complete! would you like to do anything else? \n1.add multiple students\n2.add single student\n3.add course \n4.print student transcript\n5.Exit\n")
        if(option =='5' ):
            print("Goodbye!")
        
   


   
           
