import streamlit as st 
import pandas as pd
from gp import cal_gp
import matplotlib.pyplot as plt


def main():

    options = ('Calculate Result', 'View Result', 'Print Result')
    add_selectbox = st.sidebar.selectbox('What action do you want to take', options)

    if add_selectbox == "Calculate Result":
        st.title('CALCULATE RESULT')

        number_of_course = st.text_input("Enter total number of courses", value=1)
        number_of_course = int(number_of_course)

        course_name=[]
        grade = []
        unit=[]

        for i in range(number_of_course):
            course_name_input = st.text_input(f'Enter name of course {i+1}').upper()
            unit_input = st.number_input(f"Enter number of units for course {i+1}", min_value=1)
            grade_input = st.selectbox(f"Select grade for course {i+1}", ['A', 'B', 'C', 'D', 'E', 'F'])

            course_name.append(course_name_input)
            grade.append(grade_input)
            unit.append(unit_input)
            
        if st.button('calculate'):

            total_point, total_unit, gpa, result = cal_gp(number_of_course, course_name, grade, unit)
           
 
            st.dataframe(pd.DataFrame(result))
            st.write("Total points ", total_point)
            st.write("Total unit ", total_unit)
            st.write("Grade Point Average (GPA)", f"{gpa:.2f}")

            if "Result" not in st.session_state:
                 st.session_state.Result = result

    elif add_selectbox == "View Result":

        if "Result" not in st.session_state:
            st.title("Error")
            st.write("Calculate result first to view result")

        else:
            st.title("RESULT AND ANALYSIS")
            df = st.session_state['Result']
            df = pd.DataFrame(df)
            st.dataframe(df)
            grade_count = df['Grade'].value_counts()

            # st.bar_chart(grade_count)
            fig, ax = plt.subplots()
            ax.bar(grade_count.index, grade_count.values)
            ax.set_xlabel('Grade')
            ax.set_ylabel('Count')
            ax.set_title('Grade Distribution')
            st.pyplot(fig)


if __name__ == '__main__':
    main()