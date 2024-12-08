# blueprint
# in object oriented programming, the class is the blueprint
#   --> all the classes will include features and functions
# all functions in a class will have the parameter "self"
class Student:
    # constructor function get executed by default
    def __init__(self):
        self.name = ""
        self.age = ""
        self.school = "River Academy"
        self.grade = ""
        self.teacher = ""
        self.score = []
    
    def change_detail(self):
        self.name = input("what is your name?")
        self.age = input("what is your age?")
        self.grade = input("what grade are you in?")
        self.teacher = input("who is your teacher?")
        subjects = str(input("how many subjects do you have?"))
        for subject in range(subjects):
            marks = input(f"how many marks did you get in {subject}")
            self.score.append(marks)
    
# creating object

s1 = Student()
s1.change_detail()