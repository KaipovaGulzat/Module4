#Gulzat Kaipova
#7/27/2023

# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))  # Convert the input to an integer
exam_three = int(input("Input exam grade three: "))  # Convert the input to an integer

grades = [exam_one, exam_two, exam_three]  # Added commas to create a list
sum = 0
for grade in grades:  # Changed "grade" to "grades" in the loop
    sum = sum + grade

avg = sum / len(grades)  # Corrected the variable name "grdes" to "grades"

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:  # Added a colon at the end of the elif statement
    letter_grade = "B"
elif avg >= 70 and avg < 80:  # Changed "avg > 69" to "avg >= 70"
    letter_grade = "C"  # Changed single quotes to double quotes
elif avg >= 65 and avg < 70:  # Changed "avg <= 69" to "avg >= 65"
    letter_grade = "D"

# Removed the extra colon at the end of the elif statement

for grade in grades:
    print("Exam:", grade)  # Changed '+' to ',' for printing

print("Average:", avg)  # Moved these print statements outside the loop
print("Grade:", letter_grade)

if letter_grade == "F":  # Fixed the syntax and used double equal signs for comparison
    print("Student is failing.")  # Added parentheses for Python 3.x print statement
else:
    print("Student is passing.")  # Added parentheses for Python 3.x print statement
