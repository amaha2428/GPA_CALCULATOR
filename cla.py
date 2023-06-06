import pandas as pd
class CGPACalculator:
    def __init__(self, number_of_course, course_name, score, unit):
        self.result = {
            'courses': course_name,
            'Grade': score,
            'Units': unit
        }

        for i in range(number_of_course):
            self.result['courses'].append(course_name)
            self.result['Grade'].append(score)
            self.result['Units'].append(unit)

        self.grading = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

        self.total_unit = 0
        self.total_point = 0
        self.gpa = 0

    def calculate_gpa(self):
        self.total_unit = 0
        for j in range(len(self.result['courses'])):
            grade = self.result['Grade'][j][0]
            unit = self.result['Units'][j]
            grade_point = self.grading.get(grade, 0)

            points = grade_point * unit

            self.total_unit = self.total_unit + unit
            self.total_point = self.total_point + points

        self.gpa = self.total_point / self.total_unit

    def view_result(self):
        print("Total Points:", self.total_point)
        print("Total Units:", self.total_unit)
        print("GPA:", self.gpa)

# number_of_course=1
# course_name='www'
# score = 'A'
# unit = 3
# # Create an instance of CGPACalculator
# calculator = CGPACalculator(number_of_course, course_name, score, unit)
# calculator.calculate_gpa()

# # Access GPA within the class method
# calculator.view_result()

# # Access GPA outside the class
# res = calculator.result
# df = pd.DataFrame(res)
# print( df)
