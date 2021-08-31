import os
import pandas as pd
import re

def parse_investing(data=str):
    parse_dates = ['Date']

    df = pd.read_csv(f'{os.getcwd()}\\Data\\{data}', parse_dates=parse_dates, decimal=",")
    dtypes = {'Price': 'float', 'Open': 'float', 'High': 'float', 'Low': 'float', 'Change %': 'float'}

    for col, types in dtypes.items():
        df[col] = df[col].apply(lambda string: re.search('([\d\,\.\-]+)', string).group(1).replace(',', '') 
                                if re.search('([\d\,\.]+)', string) != None else None)

        df[col] = df[col].astype(types)
    df.sort_values(by='Date', ascending=True, inplace=True)

    return df