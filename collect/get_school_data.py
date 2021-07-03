import pandas as pd


def get_school_data(address: str):

    """
    Gets school data given the address
    :param address: str of file location (*.xlsx)
    :return: pd.DataFrame of school data needed for further analysis
    """

    cols = ['woj', 'pow', 'gm', 'Województwo', 'Powiat', 'Gmina', 'Typ gminy', 'Typ', 'Nazwa typu',
            'Uczniowie, wychow., słuchacze', 'Nauczyciele pełnozatrudnieni',
            'Nauczyciele niepełnozatrudnieni (stos.pracy)',
            'Nauczyciele niepełnozatrudnieni (w etatach)']

    df = pd.read_excel(address, usecols=cols)
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)

    return df
