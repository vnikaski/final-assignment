import pandas as pd
import numpy as np

def get_students_per_school(df: pd.DataFrame, df2: pd.DataFrame):

    # traditional ages of attendance in schools (for schools that are clear to classify)

    ages = {'Bednarska Szkoła Realna': [16, 17, 18],
            'Branżowa szkoła I stopnia': [16, 17, 18],
            'Czteroletnie liceum plastyczne': [16, 17, 18],
            'Dziewięcioletnia ogólnokształcąca szkoła baletowa': [10, 11, 12, 13, 14, 15, 16, 17, 18],
            'Dziewięcioletnia szkoła sztuki tańca': [10, 11, 12, 13, 14, 15, 16, 17, 18],
            'Gimnazjum': [15],
            'Liceum ogólnokształcące': [16, 17, 18],
            'Ogólnokształcąca szkoła muzyczna I stopnia': [7, 8, 9, 10, 11, 12],
            'Ogólnokształcąca szkoła muzyczna II stopnia': [13, 14, 15, 16, 17, 18],
            'Poznańska szkoła chóralna': [7, 8, 9, 10, 11, 12, 13, 14],
            'Przedszkole': [4, 5, 6],
            'Punkt przedszkolny': [4, 5, 6],
            'Sześcioletnia ogólnokształcąca szkoła sztuk pięknych': [13, 14, 15, 16, 17, 18],
            'Sześcioletnia szkoła sztuki tańca': [13, 14, 15, 16, 17, 18],
            'Szkoła podstawowa': [7, 8, 9, 10, 11, 12, 13, 14],
            'Technikum': [16, 17, 18, 19],
            'Zespół wychowania przedszkolnego': [4, 5, 6]}

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

    # we have to subtract two years due to reference difference in files
    for school in ages:
        ages[school] = [x + 2 for x in ages[school]]

    # preparing the result file
    res = pd.DataFrame({'Nazwa typu': sorted(list(ages.keys()) * 2),
                        'Typ obszaru': ['miejski', 'wiejski'] * len(ages)})

    res[[x for x in range(6, 22)]] = np.zeros((len(ages) * 2, 16))

    for school in ages:
        all_students_U = df.loc[df['Nazwa typu'] == school].loc[df['Typ gminy'] == 'M'][
            'Uczniowie, wychow., słuchacze'].sum()
        all_students_R = df.loc[df['Nazwa typu'] == school].loc[df['Typ gminy'] == 'Gm'][
            'Uczniowie, wychow., słuchacze'].sum()

        all_potential = df2.loc[df2['age'].isin(ages[school])].sum()
        # let's assume the kids are born evenly throughout the year
        for i in range(len(ages[school])):
            res.at[res.loc[(res['Nazwa typu'] == school) & (res['Typ obszaru'] == 'miejski')].index, ages[school][i]] = \
            ((df2.loc[df2['age'] == ages[school][i]]['urban'] / all_potential['urban']) * all_students_U).values[0]
            res.at[res.loc[(res['Nazwa typu'] == school) & (res['Typ obszaru'] == 'wiejski')].index, ages[school][i]] = \
            ((df2.loc[df2['age'] == ages[school][i]]['rural'] / all_potential['rural']) * all_students_R).values[0]

    res.columns = list(res.columns[:2]) + [2020 - x for x in res.columns[2:]]

    res.to_csv('students_per_school_by_year_of_birth_and_district_type.csv')