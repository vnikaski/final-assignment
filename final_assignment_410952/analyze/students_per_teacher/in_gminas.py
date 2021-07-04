from final_assignment_410952.analyze.students_per_teacher.get_basic_statistics import get_basic_statistics
import pandas as pd


def in_gminas(df: pd.DataFrame):
    grouped = df.groupby(['code', 'Typ'])
    res = grouped[['Województwo', 'Powiat', 'Gmina', 'Nazwa typu']].first().reset_index()
    res['Avg'], res['Min'], res['Max'] = get_basic_statistics(grouped)

    return res[['Województwo', 'Powiat', 'Gmina', 'Typ', 'Nazwa typu', 'Min', 'Avg', 'Max']]


