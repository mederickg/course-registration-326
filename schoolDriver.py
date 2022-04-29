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
        
        
        
class Course:
    """ Course class representing a specific course in the school. Contains
    information on the course.

    Attributes:
        courseName (str): A string representation of the course name.
        sections (list): A list of Section objects.
        prereqs (list): A list of Course objects needed to be completed
        to be able to take this current course.
    """
    
    def __init__(self, courseName,sections,prereqs):
        """ Initializes an instance of a Course
        
        Args:
            courseName (str): A string representation of the course name.
            sections (Section): A Section objects.
            prereqs (Course): A Course object needed to be completed
            to be able to take this current course.
            
        Side effects: sets the Course class attributes.
        """
        
        self.courseName=courseName
        self.sections= sections
        self.prereqs = prereqs
        
class Section:
    """ Section class representing a specific section in the course. Contains
    information on the section.

    Attributes:
        sectionNumber (int): The section number
        instructor (str): A string representation of the instructor's name.
        time (str): A string representation of the time the class starts.
        Assuming each class is 50 minutes long.
    """
    
    def __init__(self,sectionNumber,instructor,time):
        """ Initializes an instance of a Section
        
        Args:
            sectionNumber (int): The section number
            instructor (str): A string representation of the instructor's name.
            time (str): A string representation of the time the class starts.
            Assuming each class is 50 minutes long.
            
        Side effects: sets the Section class attributes.
        """
        
        self.sectionNumber = sectionNumber
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