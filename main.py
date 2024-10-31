import pandas as pd

# create a df
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


def transform(df):
    df['C'] = df['A'] + df['B']
    return df

