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