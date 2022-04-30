import pandas as pd 

class Register:
    def __init__(self,transcript,course_db):
        self.transcript = pd.read_csv(transcript)
        self.course_db = pd.read_csv(course_db)
        self.schedule = pd.DataFrame()
    
    def add(self,prefix,course_num,section_num): 
       pfx_filt =  self.course_db["Prefix"] == prefix 
       course_num_filt = self.course_db["Course number"] == course_num 
       sec_num_filt = self.course_db["Section number"] == section_num
       combined_filter = pfx_filt & sec_num_filt & course_num_filt
       
       entry = self.course_db[combined_filter]
    
       self.schedule = pd.concat([self.schedule,entry])
       self.schedule = self.schedule.drop(columns=['Credits needed'])
    
    def drop(self, courseName):
        self.schedule = self.schedule.drop([courseName], axis = 0)
        
    def verify_credits():
        pass
    
    def verify_time():
        pass 
    
    def print_schedule(self):
        return self.schedule.head()
    
    
class Course_db():
    
    def __init__(self, path):
        self.courses = pd.read_csv(path)
    
    def add_courses(self, path): 
        temp = pd.read_csv(path)
        self.courses = pd.concat([self.courses, temp])
