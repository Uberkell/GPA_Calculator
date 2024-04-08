'''
William Class IV
william.class@ndus.edu
CSCI 160
Program 5
'''
studentGPA = 0.0 #Here is define and set all the defalt values for used for all the functions
totalCredits = 0
totalHonor = 0
totalClasses = 0
creditsPassed = 0
classesPassed = 0
while True:#Here i create the loop to keep checking for a class name
    className = input("Enter the Class name: ")
    if className == "":
        break
    else:
        totalClasses = totalClasses + 1
        creditNumb = int(input("Enter the number of credits this class has: "))
        totalCredits= totalCredits + creditNumb
        classGrade = str(input("Enter your grade for that class: "))
        if classGrade == "A" or classGrade == "a": #Here is a series of if and elif statments that records passed credits, passed classes, and gpa
            totalHonor = totalHonor + 4.0
            creditsPassed = creditsPassed + creditNumb
            classesPassed = classesPassed + 1
        elif classGrade == "B" or classGrade == "b":
            totalHonor = totalHonor + 3.0
            creditsPassed = creditsPassed + creditNumb
            classesPassed = classesPassed + 1
        elif classGrade == "C" or classGrade == "c":
            totalHonor = totalHonor + 2.0
            creditsPassed = creditsPassed + creditNumb
            classesPassed = classesPassed + 1
        elif classGrade == "D" or classGrade == "D":
            totalHonor = totalHonor + 1.0
            creditsPassed = creditsPassed + creditNumb
            classesPassed = classesPassed + 1
        elif classGrade == "F" or classGrade == "f":
            totalHonor = totalHonor + 0.0      
studentGpa = totalHonor / totalClasses #This is the gpa calculation

print(format("GPA:", "25s"),format(studentGpa, "5.3f"))# Here all the formated print statments showing the output
print(format("Credits attempted:", "25s"), format(totalCredits, "5d"))
print(format("Credits passed:", "25s"), format(creditsPassed, "5d"))
print(format("Classes attempted:", "25s"), format(totalClasses, "5d"))
print(format("Classes passed:", "25s"), format(classesPassed, "5d"))
    
        