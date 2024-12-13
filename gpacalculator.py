num_courses = int(input("Enter the number of courses:"))

total_points = 0
total_credits = 0

for i in range(num_courses):
    credits = float(input(f"Enter the number of credits for course {i+1}:"))
    grade = input(f"Enter grade for course {i+1}:").upper()
    
    if grade == 'A':
        grade_point = 4.0
    elif grade == 'A-':
        grade_point = 3.7
    elif grade == 'B+':
        grade_point = 3.3
    elif grade == 'B':
        grade_point = 3.0
    elif grade == 'B-':
        grade_point = 2.7
    elif grade == 'C+':
        grade_point = 2.3
    elif grade == 'C':
        grade_point = 2.0
    elif grade == 'C-':
        grade_point = 1.7
    elif grade == 'D+':
        grade_point = 1.3
    elif grade == 'D':
        grade_point = 1.0
    elif grade == 'F':
        grade_point = 0.0
    else:
        print("Invalid grade entered. Please enter a valid grade (A, B+, C, etc.).")
        continue
    
    total_points += grade_point * credits
    
    total_credits += credits

if total_credits > 0:
    gpa = total_points / total_credits
    print(f"Your GPA is: {gpa:.2f}")
else:
    print("No valid courses entered.")
