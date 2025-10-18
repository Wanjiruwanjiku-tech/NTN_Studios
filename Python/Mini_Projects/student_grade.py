# Student Grade Management System.
# A simple console-based system that allows the user to manage students and their grades.

class Student:
    def __init__(self, name, student_id, ):
        self.name = name
        self.student_id = student_id
        self. grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
