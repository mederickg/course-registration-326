import pandas as pd

class Register:
    def __init__():
        pass
    
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
    
cs1 = Course_db("sample_data.csv")

cs1.add_courses("sample_data_2.csv")

print(cs1.courses)