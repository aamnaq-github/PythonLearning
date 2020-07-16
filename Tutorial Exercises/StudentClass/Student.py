import random

class StudentClass:
    # initialize function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def age(self):
        return random.randint(20, 50)

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False