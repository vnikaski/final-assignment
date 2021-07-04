import pandas as pd


def prepare_res_df(ages)->pd.DataFrame:

    res = pd.DataFrame({'Nazwa typu': sorted(list(ages.keys()) * 16),
                        'Rok urodzenia': [2020 - x for x in range(6, 22)] * len(ages),
                        'Obszar wiejski MIN': [0 for x in range(6, 22)] * len(ages),
                        'Obszar wiejski AVG': [0 for x in range(6, 22)] * len(ages),
                        'Obszar wiejski MAX': [0 for x in range(6, 22)] * len(ages),
                        'Obszar miejski MIN': [0 for x in range(6, 22)] * len(ages),
                        'Obszar miejski AVG': [0 for x in range(6, 22)] * len(ages),
                        'Obszar miejski MAX': [0 for x in range(6, 22)] * len(ages)})

    return res