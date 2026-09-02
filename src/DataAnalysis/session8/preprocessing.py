def get_type_Info(df):
    return pd.DataFrame({
        'dtypes': df.dtypes,
        'nunique': df.nunique()
    }).T