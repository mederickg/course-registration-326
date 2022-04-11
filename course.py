class Course:
    
    def __init__(self, courseName,sections):
        self.courseName=courseName
        self.sections= sections
        
class Section:
    
    def __init__(self,instructor,time):
        self.instructor= instructor
        self.time = time