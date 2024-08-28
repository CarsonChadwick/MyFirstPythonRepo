from datetime import datetime

class Student :
    university_name = "CP University"
    next_id = 1

    def __init__(self, first_name, last_name) :
        self.first_name = first_name
        self.last_name = last_name
        self.stud_id = Student.next_id
        Student.next_id = Student.next_id + 1 
        self.course = None
        self.total_credits = 0

    def get_info(self) :
        return ("Student " + str(self.stud_id) + " " + self.first_name + " " + self.last_name + " total credits are " + str(self.total_credits))
    
class Course :
    def __init__(self, course_num, course_title, course_credits, student_owner) :
        self.course_num = course_num
        self.course_title = course_title
        self.course_credits = course_credits
        self.passed_course = False
        self.final_exam = Final_Exam(self, student_owner)

class Final_Exam :
    def __init__ (self, course_owner, student_owner) :
        self.test_datetime = None
        self.test_location = ""
        self.test_score = 0
        self.course_owner = course_owner
        self.student_owner = student_owner

    def set_test(self, test_datetime, test_location, test_score) :
            self.test_datetime = test_datetime
            self.test_location = test_location
            self.course_owner.passed_course = self.pass_course(test_score)
    
    def pass_course(self, test_score) :
        self.test_score = test_score

        if (test_score >= 75) :            
            self.student_owner.total_credits = self.student_owner.total_credits + self.course_owner.course_credits
            return True
        else :
            return False
        

sFirst_name = input("Enter the student first name: ")
sLast_name = input("Enter the student's last name: ")

oStudent = Student(sFirst_name, sLast_name)

sCourse_num = input("\nEnter " + oStudent.first_name + "'s favorite course num: " )
sCourse_Desc = input("Enter " + sCourse_num + "'s title: ")
iCredits = int(input("Enter the number of credits for " + sCourse_Desc + ": "))

oStudent.course = Course(sCourse_num, sCourse_Desc, iCredits, oStudent)

dTestDate = datetime.strptime(input("\nWhat was the final exam date for " + oStudent.course.course_title + ": "), "%m/%d/%Y")
sLocation = input("What was the test location: ")
iScore = int(input("What was the final exam score: "))

oStudent.course.final_exam.set_test(dTestDate,sLocation, iScore)

print("\n" + oStudent.get_info() + "\n\n")