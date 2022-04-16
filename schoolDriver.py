class School:
    """School class is the class that runs the functionalities of the school using the classes and functions of students and faculty.
    courses. 
    
    Attributes: students(list): list of students in the school 
                courses(list): list of courses offered
                faculty(list): list of schools faculty members
                 
    """
    def __init__(self,students,courses,faculty):
        """init method defines the attributes based on user input
        
            Side Effects: school attributes instantiated
        """
        self.students= students
        self.courses= courses
        self.faculty=faculty
    
    def add_course():
        """adds a course to the school from argparser perspective
        
        Side effects: courses attribute is added to"""
        pass
        
    def addStudents(filepath):
        """Reads in a formatted file of students, constructs them, and adds them to the students at the school
        
        regex + reading in  from file"""
        pass
        
        #with open(filepath,'r',encoding='utf-8') as file:
        #    for line in file:
        
    def print_transcript(Student = None):
        """prints a transcript of either  a given student, or the raw formatting of a blank transcript
        
            Returns: String representation of a transcript for a student"""
        pass
    
    if __name__ == "__main__":
        """driver of the school class, works to build a school, allow a user to choose their perspective of the school, and work with the commands
        they would have access to"""
        pass
        
    def student_stats(year):
        """provides a statistical representation of the student gpa of a certain class of students."""
        pass
    def class_rankings():
        """prints the 5 highest ranked students in the class, based on gpa, returns sorted list of the students based on gpa,descending
        
        Returns: sorted list of students in descending order based on gpa"""
        pass
        
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
        """initializes a person object

        Args:
            name (str): name of person
            age (int): person's age
        """
        self.name=name
        self.age=age
        
class Student(Person):
    
    def __init__(self,year,schedule):
        """initializes a student object

        Args:
        year (int): year that the student is in
        schedule (str): path to a file containing student schedule
        """
        super.__init__()
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
        """initializes Intructor object

        Args:
            courses (str): path to a file containing courses
        """
        super.__init__(self)
        self.courses=courses
        
    def give_grade():
        """
        Method takes a given student, and assigns them a final grade for a course
        
        Side Effects: impacts the students gpa calculation
        """
        pass
               
if __name__ == "__main__":
        pass     
        