import pandas as pd

class Student:
    def __init__ (self, name, gender, lunch, math_score, reading_score, writing_score):
        self.name = name
        self.gender = gender
        self.lunch = lunch
        self.math_score = math_score
        self.reading_score = reading_score
        self.writing_score = writing_score

    def calculated_grade(self):
        print(f"Calculated Grade was: {(self.math_score + self.writing_score + self.reading_score)/3}")

class WellFedStudent(Student):
    def __init__(self, name, gender, lunch, math_score, reading_score, writing_score):
        super().__init__(name, gender, lunch, math_score, reading_score, writing_score)

    def calculated_grade(self):
        print(f"Calculated Grade was: {((self.math_score + self.writing_score + self.reading_score)/3)*3}")

studentList = []
df = pd.read_excel("study_performance.xlsx")
print(df)

for index, row in df.iterrows():
    if row["lunch"] == "standard" :
        oStudent = WellFedStudent(row["name"], row["gender"], row["lunch"], row["math_score"], row["reading_score"], row["writing_score"])
    else:
        oStudent = Student(row["name"], row["gender"], row["lunch"], row["math_score"], row["reading_score"], row["writing_score"])
    studentList.append(oStudent)

for student in studentList:
    if(student.math_score>=76) :
        student.calculated_grade()
    else:
        print("This student didn't do to well.")