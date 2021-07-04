from analyze.students_per_teacher.get_basic_statistics import get_basic_statistics
import pandas as pd

def in_types(df: pd.DataFrame):
    grouped = df.groupby(['Typ gminy', 'Typ'])
    res = grouped['Nazwa typu'].first().reset_index()
    res['Avg'], res['Min'], res['Max'] = get_basic_statistics(grouped)

    return res[['Typ gminy', 'Typ', 'Nazwa typu', 'Min', 'Avg', 'Max']]