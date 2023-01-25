''' 
Diana Kang
AD540
Program that accepts student's percent range as a keyboard input and output GPA using If/Else statements.
Upon running the file, the user is prompted (input) to insert their grade as percentage (0% - 100%). 
The program then calculates the range the grade falls into.
'''

name = input("Name: ")
percent = float(input("Percent: "))

if percent >= 95.0:
    gpa = 4.0
elif percent >= 94.0:
    gpa = 3.9
elif percent >= 93.0:
    gpa = 3.8
elif percent >= 92.0:
    gpa = 3.7
elif percent >= 91.0:
    gpa = 3.6
elif percent >= 90.0:
    gpa = 3.5
elif percent >= 89.0:
    gpa = 3.4
elif percent >= 88.0:
    gpa = 3.3
elif percent >= 87.0:
    gpa = 3.2
elif percent >= 86.0:
    gpa = 3.1
elif percent >= 85.0:
    gpa = 3.0
elif percent >= 84.0:
    gpa = 2.9
elif percent >= 83.0:
    gpa = 2.8
elif percent >= 82.0:
    gpa = 2.7
elif percent >= 81.0:
    gpa = 2.6
elif percent >= 80.0:
    gpa = 2.5
elif percent >= 79.0:
    gpa = 2.4
elif percent >= 78.0:
    gpa = 2.3
elif percent >= 77.0:
    gpa = 2.2
elif percent >= 76.0:
    gpa = 2.1
elif percent >= 75.0:
    gpa = 2.0
elif percent >= 74.0:
    gpa = 1.9
elif percent >= 73.0:
    gpa = 1.8
elif percent >= 72.0:
    gpa = 1.7
elif percent >= 71.0:
    gpa = 1.6
elif percent >= 70.0:
    gpa = 1.5
elif percent >= 69.0:
    gpa = 1.4
elif percent >= 68.0:
    gpa = 1.3
elif percent >= 67.0:
    gpa = 1.2
elif percent >= 66.0:
    gpa = 1.1
elif percent >= 65.0:
    gpa = 1.0
else:
    gpa = 0.0

print(name + "'s GPA is: " + str(gpa))
