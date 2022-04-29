import pandas as pd 

class Register:
    def __init__(self,transcript,course_db):
        self.transcript = pd.read_csv(transcript)
        self.course_db = pd.read_csv(course_db)
        self.schedule = pd.DataFrame()
    
    def add(): 
        pass
    
    def drop(self, courseName):
        self.schedule = self.schedule.drop([courseName], axis = 0)
        
    
    def verify_credits():
        pass
    
    def verify_time():
        pass 
    
    def print_schedule():
        pass 
    
    
class Course_db():
    
    def __init__(self, path):
        self.courses = pd.read_csv(path)
    
    def add_courses(self, path): 
        temp = pd.read_csv(path)
        self.courses = pd.concat([self.courses, temp])
    
if __name__ == "__main__":
    cs1 = Course_db("sample_data.csv")

    cs1.add_courses("sample_data_2.csv")

    print(cs1.courses)