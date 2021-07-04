import pandas as pd


def get_inhabitants_data(address: str):
    """
    Return inhabitants_data given the adress
    :param address: str, address of excel file containing inhabitants data
    :return: pd.DataFrame, inhabitants data for further analysis
    """
    names = ['age', 'urban', 'rural']

    while True:
        try:
            df = pd.read_excel(address, header=5, usecols=[0, 4, 7], names=names)
            break
        except ValueError:
            print('Please check if your data files contains all of the columns listed below:'
                  '\n-Age column on 0th position'
                  '\n-Number of inhabitants in urban areas on 4th position'
                  '\n-Number of inhabitants in rural areas on 7th position')

    df = df.dropna(how='all').reset_index(drop=True)

    return df
