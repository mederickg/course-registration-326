class Course:
    
    def __init__(self, courseName,sections,prereqs):
        self.courseName=courseName
        self.sections= sections
        self.prereqs = prereqs
        
class Section:
    
    def __init__(self,instructor,time):
        self.instructor= instructor
        self.time = time