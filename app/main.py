import pandas as pd

# create a df
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


def transform(df):
    """
    Transforms the input DataFrame by adding a new column 'C' which is the sum of columns 'A' and 'B'.

    Parameters:
    df (pandas.DataFrame): The input DataFrame with columns 'A' and 'B'.

    Returns:
    pandas.DataFrame: The transformed DataFrame with the new column 'C'.
    """
    df['C'] = df['A'] + df['B']
    return df

