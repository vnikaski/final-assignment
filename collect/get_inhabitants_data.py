import pandas as pd


def get_inhabitants_data(address: str):
    """
    Return inhabitants_data given the adress
    :param address: str, address of excel file containing inhabitants data
    :return: pd.DataFrame, inhabitants data for further analysis
    """

    names = ['age', 'urban', 'rural']
    df = pd.read_excel(address, header=5, usecols=[0, 4, 7],
                       names=names).dropna(how='all').reset_index(drop=True)
    return df
