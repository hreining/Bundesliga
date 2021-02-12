import pandas as pd

def rename_cols(df: pd.DataFrame, old: list, new: list) -> pd.DataFrame:

    for i in range(0,len(old),1):
        df.rename(columns={old[i] : new[i]}, inplace=True)

    return(df)