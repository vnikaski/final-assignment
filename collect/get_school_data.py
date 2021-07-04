import pandas as pd

def get_school_data(address: str, communicats: bool = True):

    """
    Gets school data of:
    - first 6-digits of teritorial code (województwo, powiat, gmina) e.g. 020401 of school location
    - names of Województwo, Powiat Gmina of school location
    - type of Gmina the school is in
    - type of the school (code)
    - type of the school (name)
    - number of students in school
    - number of teachers (full time positions (combined)) in school
    given the address of the file containing informatory school data
    :param address: str of file location (*.xlsx, *.xls, *.xlsm, *.xlsb, *.odf, *.ods)
    :return: pd.DataFrame of school data needed for further analysis

    :SAVES: gsd_summary.txt file with description of data that has been dropped
    """

    cols = ['woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu',
            'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni',
            'Nauczyciele niepełnozatrudnieni (w etatach)',
            'Nr RSPO jednostki sprawozdawczej']

    if communicats:
        print('collecting the data...')

    while True:
        try:
            df = pd.read_excel(address, usecols=cols,
                               converters={'woj': '{:0>2}'.format,
                                           'pow': '{:0>2}'.format,
                                           'gm': '{:0>2}'.format})
            break
        except ValueError:
            print("Data file does not contain expected columns. Please provide a file containing all of the below:"
                  "\n'woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu', "
                  "'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni', "
                  "'Nauczyciele niepełnozatrudnieni (w etatach)'")

    df = df.dropna().reset_index(drop=True)
    initial_size = len(df)

    df['teachers'] = df['Nauczyciele pełnozatrudnieni'] + df['Nauczyciele niepełnozatrudnieni (w etatach)']
    df['code'] = df['woj'] + df['pow'] + df['gm']

    if communicats:
        print('preparing teritorial code...')

    # finishing the teritorial code
    for i in range(len(df)):
        if df.iloc[i]['Typ gminy'] == 'M':
            df.at[i, 'code'] += '1'
        elif df.iloc[i]['Typ gminy'] == 'Gm':
            df.at[i, 'code'] += '2'
        elif df.iloc[i]['Typ gminy'] == 'M-Gm':
            df.at[i, 'code'] += '3'

    df = df.drop(columns=['woj', 'pow', 'gm', 'Nauczyciele pełnozatrudnieni', 'Nauczyciele niepełnozatrudnieni (w etatach)'])

    if communicats:
        print('reducing affiliated schools...')

    # technically this loop is needed only for students_per_teacher by the type of school, but it will not mess with
    # any other operation at the same time reducing the size of df
    reduced = 0
    for RSPO in df['Nr RSPO jednostki sprawozdawczej']:
        n_teachers = df.loc[df['Nr RSPO jednostki sprawozdawczej'] == RSPO, 'teachers'].sum()
        n_students = df.loc[df['Nr RSPO jednostki sprawozdawczej'] == RSPO, 'Uczniowie, wychow., słuchacze'].sum()
        for row_id in df.loc[df['Nr RSPO jednostki sprawozdawczej'] == RSPO].index:
            students = df.iloc[row_id]['Uczniowie, wychow., słuchacze']
            if students == 0:
                if df.iloc[row_id]['teachers'] != 0:
                    reduced += 1
                df.at[row_id, 'teachers'] = 0
            elif n_students != 0:
                df.at[row_id, 'teachers'] = n_teachers * (students / n_students)

    if communicats:
        print('excluding empty schools...')

    # we do not count empty schools as they are not useful in the statistics (keep in mind, that part of those come from 'reduced')
    empty = len(df.loc[(df['teachers'] == 0) & (df['Uczniowie, wychow., słuchacze'] == 0)]) - reduced
    df = df.drop(df.loc[(df['teachers'] == 0) & (df['Uczniowie, wychow., słuchacze'] == 0)].index)

    if communicats:
        print('checking for potential errors...')

    # unafilliated schools with no teachers (potential errors in data)
    err = len(df.loc[df['teachers'] == 0])
    df = df.drop(df.loc[df['teachers'] == 0].index)

    df = df.drop(columns=['Nr RSPO jednostki sprawozdawczej'])

    inf = open('gsd_summary.txt', 'w+')
    inf.write(f"Collecting school data from the address: {address} following decisions were made:\n"
              f"{reduced} ({(reduced/initial_size)*100}% of initial data size) instances of school affiliation types "
              f"were reduced to they subtypes for further analysis\n"
              f"{empty} ({(empty/initial_size)*100}% of initial data size) instances of schools with no teachers and "
              f"no students were not included in further analysis\n"
              f"{err} ({(err/initial_size)*100}% of initial data size) instances of schools with no teachers (with "
              f"students) were not included in further analysis as a potential error")
    inf.close()

    return df
