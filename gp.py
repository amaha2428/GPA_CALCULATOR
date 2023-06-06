def cal_gp(number_of_course, course_name, score, unit):
    result = {
        'courses': [],
        'Grade': [],
        'Units': []
    }

    for i in range(number_of_course):
        result['courses'].append(course_name[i])
        result['Grade'].append(score[i])
        result['Units'].append(unit[i])


    grading = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}

    total_unit = 0
    total_point =0 
    for j in range(len(result['courses'])):
        grade = result['Grade'][j]
        unit = result['Units'][j]
        grade_point = grading.get(grade, 0)

        points = grade_point * unit

        total_unit+=unit
        total_point+=points

    gpa = total_point / total_unit
    
    return total_point, total_unit, gpa, result

