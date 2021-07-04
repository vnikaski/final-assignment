from final_assignment_410952.analyze.students_per_school.report_used_data import report_used_data
from final_assignment_410952.analyze.students_per_school.prepare_res_df import prepare_res_df
from final_assignment_410952.analyze.students_per_school.calculate_basic_statistics_by_year import calculate_basic_statistics_by_year
import pandas as pd


def get_students_per_school(df: pd.DataFrame, df2: pd.DataFrame):
    """

    :param df:
    :param df2:
    :return:
    """

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

    report_used_data(df, ages)

    # we have to subtract two years due to reference difference in files
    for school in ages:
        ages[school] = [x + 2 for x in ages[school]]

    # preparing the result file
    res = prepare_res_df(ages)

    all_ages = [x for x in range(6, 22)]
    kids_in_range = df2.loc[df2['age'].isin(all_ages)].sum()

    rural_year_share = [df2.loc[df2['age'] == x]['rural'].values[0] / kids_in_range['rural'] for x in range(6, 22)]
    urban_year_share = [df2.loc[df2['age'] == x]['urban'].values[0] / kids_in_range['urban'] for x in range(6, 22)]

    res = calculate_basic_statistics_by_year(ages, rural_year_share, urban_year_share, df, res)

    res.to_csv('students_per_school_by_year_of_birth_and_district_type.csv')