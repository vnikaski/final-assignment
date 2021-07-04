from analyze.students_per_teacher.in_gminas import in_gminas
from analyze.students_per_teacher.in_types import in_types
import pandas as pd

def get_results(df: pd.DataFrame):
    df['students per teacher'] = df['Uczniowie, wychow., słuchacze'] / df['teachers']
    in_gminas(df).to_csv('student_per_teacher_in_gminas_by_school_types.csv')
    in_types(df).to_csv('student_per_teacher_in_types_of_district_by_school_types.csv')






