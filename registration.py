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
    
    def create_course(): 
        pass 
    
    def create_section():
        pass 
    
    
cs1 = Course_db("sample_data.csv")
print(cs1.courses)