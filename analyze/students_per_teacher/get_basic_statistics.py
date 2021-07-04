import pandas as pd

def get_basic_statistics(grouped):
    res = pd.DataFrame()
    res['type_id'] = grouped.groups.keys()
    mean = grouped['students per teacher'].mean().values
    min = grouped['students per teacher'].max().values
    max = grouped['students per teacher'].min().values
    return mean, min, max
