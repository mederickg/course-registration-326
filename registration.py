import pandas as pd 

class Register:
    def __init__(self,transcript,course_db):
        self.transcript = pd.read_csv(transcript)
        self.course_db = pd.read_csv(course_db)
        self.schedule = pd.DataFrame()
    
    def add(): 
        pass
    
    def drop():
        pass 
    
    def verify_credits():
        pass
    
    def verify_time():
        pass 
    
    def print_schedule():
        pass 
    
    def can_walk():
        pass 
    
class Course_db():
    
    def __init__(self, path):
        self.courses = pd.read_csv(path)
    
    def add_courses(self, path): 
        temp = pd.read_csv(path)
        self.courses = pd.concat([self.courses, temp])
