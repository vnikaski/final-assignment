import pandas as pd


def calculate_basic_statistics_by_year(ages: dict,
                                       rural_year_share: list,
                                       urban_year_share: list,
                                       df: pd.DataFrame,
                                       res: pd.DataFrame):
    for school in ages:
        for i in range(len(rural_year_share)):
            if 6 + i in ages[school]:
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar wiejski MIN'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'Gm')][
                        'Uczniowie, wychow., słuchacze'].min() * rural_year_share[i]
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar wiejski AVG'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'Gm')][
                        'Uczniowie, wychow., słuchacze'].mean() * rural_year_share[i]
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar wiejski MAX'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'Gm')][
                        'Uczniowie, wychow., słuchacze'].max() * rural_year_share[i]
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar miejski MIN'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'M')][
                        'Uczniowie, wychow., słuchacze'].min() * urban_year_share[i]
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar miejski AVG'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'M')][
                        'Uczniowie, wychow., słuchacze'].mean() * urban_year_share[i]
                res.at[res.loc[(res['Nazwa typu'] == school) & (res['Rok urodzenia'] == 2020 - (6 + i))].index,
                       'Obszar miejski MAX'] = \
                    df.loc[(df['Nazwa typu'] == school) & (df['Typ gminy'] == 'M')][
                        'Uczniowie, wychow., słuchacze'].max() * urban_year_share[i]
    res = res.fillna(0)
    return res