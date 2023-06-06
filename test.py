import pandas as pd
Result = []
result = {
    'courses': [],
    'Grade': [],
    'Units': []
}

number_of_course = 3
for i in range(number_of_course):
    course_name = input(f'enter course {i+1}: ').upper()
    score = input("Enter grade: ").upper()
    unit = int(input(f'course {i+1} unit : '))
    result['courses'].append(course_name)
    result['Grade'].append(score)
    result['Units'].append(unit)


grading = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}

print(result)

total_unit = 0
total_point =0 
for j in range(len(result['courses'])):
    grade = result['Grade'][j]
    unit = result['Units'][j]
    grade_point = grading.get(grade, 0)

    points = grade_point * unit

    total_unit+=unit
    total_point+=points

print(total_point, total_unit)

gpa = total_point / total_unit

print(gpa)
Result.append(result)
df = pd.DataFrame(Result[0])
print(df)

