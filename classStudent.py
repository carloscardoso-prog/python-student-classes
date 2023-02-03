class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    
    def on_honor_roll(self): # access the current instance of the class, and is used to access variables that belongs to the class.
        if self.gpa >= 3.5:
            return True
        else:
            return False