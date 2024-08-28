# This program will accept a student name and grading information
# and then display the calculated final average and earned letter grade

# Receives the sum of tests, quizzes, and homework scores
# and the weighting pct of tests, quizzes, and homework scores
# and calculates the final average and determines the earned letter grade
# returns the letter grade concatenated with the final average
# For example, A with an average of 94
def Determine_grade(iTestScore, fTestPct, iQuizScore, fQuizPct, iHomeworkScore, fHomeworkPct) :
    fTest = round(iTestScore * (fTestPct/100), 1)
    fQuiz = round(iQuizScore * (fQuizPct/100), 1)
    fHomework = round(iHomeworkScore * (fHomeworkPct/100), 1)
    
    fGrade = fTest + fQuiz + fHomework
    
    # 94 and above is A
    # 90 to 93 is A-
    # 87 to 89 is B+
    # 83 to 86 is B
    # 80 to 82 is B-
    # otherwise a C
    if (fGrade > 94) :
        sGrade = "A"
    elif (fGrade >= 90) :
        sGrade = "A-"
    elif (fGrade >= 87) :
        sGrade = "B+"
    elif (fGrade >= 83) :
        sGrade = "B"
    elif (fGrade >= 80) :
        sGrade = "B-"
    else :
        sGrade = "C"  
    
    return (sGrade + " with an average of " + str(fGrade)) 
sStudent = input("What is the student name? ")
iTestCount = int(input("\nHow many tests? "))
fTestPct = float(input("What percentage of the overall grade are tests worth? (i.e. 50) "))

iTestSum = 0
iQuizSum = 0
iHomeworkSum = 0
for iCount in range(1, iTestCount + 1) :
    iTestSum = iTestSum + int(input("Enter the score for test #" + str(iCount) + ": "))
iTestSum = iTestSum / iTestCount

iQuizCount = int(input("\nHow many quizzes? "))
fQuizPct = float(input("What percentage of the overall grade are quizzes worth? (i.e. 20) "))

for iCount in range(1, iQuizCount + 1) :
    iQuizSum = iQuizSum + int(input("Enter the score for quiz #" + str(iCount) + ": "))
iQuizSum = iQuizSum / iQuizCount

iHomeworkCount = int(input("\nHow many homework assignments? "))
fHomeworkPct = float(input("What percentage of the overall grade are homework assignments worth? (i.e. 30) "))

for iCount in range(1, iHomeworkCount + 1) :
    iHomeworkSum = iHomeworkSum + int(input("Enter the score for homework #" + str(iCount) + ": "))
iHomeworkSum = iHomeworkSum / iHomeworkCount

sGrade = Determine_grade(iTestSum, fTestPct, iQuizSum, fQuizPct, iHomeworkSum, fHomeworkPct) 
#def Determine_grade(iTestScore, fTestPt, iQuizScore, iHomeworkScore, fHomeworkPct) :
print("\n" + sStudent + " received a(n) " + sGrade)
