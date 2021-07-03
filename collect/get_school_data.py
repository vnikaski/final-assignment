import pandas as pd


def get_school_data(address: str):

    """
    Gets school data of:
    - 6-digits teritorial code (województwo, powiat, gmina) e.g. 020401 of school location
    - names of Województwo, Powiat Gmina of school location
    - type of Gmina the school is in
    - name of type of Gmina the school is in
    - number of students in school
    - number of teachers (full time positions (combined))
    given the address of the file containing informatory school data
    :param address: str of file location (*.xlsx, *.xls, *.xlsm, *.xlsb, *.odf, *.ods)
    :return: pd.DataFrame of school data needed for further analysis
    """

    cols = ['woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu',
            'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni',
            'Nauczyciele niepełnozatrudnieni (stos.pracy)',
            'Nauczyciele niepełnozatrudnieni (w etatach)']

    while True:
        try:
            df = pd.read_excel(address, usecols=cols)
            df = df.dropna(how='all')
            df = df.reset_index(drop=True)
            return df
        except ValueError:
            print("Data file does not contain expected columns. Please provide a file containing all of the below:"
                  "\n'woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu', "
                  "'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni', "
                  "'Nauczyciele niepełnozatrudnieni (stos.pracy)', 'Nauczyciele niepełnozatrudnieni (w etatach)'")