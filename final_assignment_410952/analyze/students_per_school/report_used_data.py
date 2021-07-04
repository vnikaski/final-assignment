import pandas as pd

def report_used_data(df: pd.DataFrame, ages: dict):
    students = df.groupby('Nazwa typu')['Uczniowie, wychow., słuchacze'].sum()
    kept = 0
    for school in ages:
        kept += students[school]

    # reporting used data
    inf = open('gsps_summary.txt', 'w+')
    inf.write(f"Due to the problems with establishing students' age in some of the school types only the following"
              f"were subjected in further analysis: \n {list(ages.keys())} \n"
              f"Above types contained {(kept/students.sum())*100}% of all of the students.")
    inf.close()