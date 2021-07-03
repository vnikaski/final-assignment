import pandas as pd


def get_school_data(address: str):

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
    """

    cols = ['woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu',
            'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni',
            'Nauczyciele niepełnozatrudnieni (w etatach)']

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

    df['location_code'] = df['woj'] + df['pow'] + df['gm']
    df['teachers'] = df['Nauczyciele pełnozatrudnieni'] + df['Nauczyciele niepełnozatrudnieni (w etatach)']

    df = df.drop(columns=['woj', 'pow', 'gm', 'Nauczyciele pełnozatrudnieni', 'Nauczyciele niepełnozatrudnieni (w etatach)'])

    return df
