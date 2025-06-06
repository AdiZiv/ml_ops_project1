import pandas as pd


def extract_datetime_features(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name])
    df['year'] = df[column_name].dt.year
    df['month'] = df[column_name].dt.month
    df['hour'] = df[column_name].dt.hour
    df['weekday'] = df[column_name].dt.weekday
    return df