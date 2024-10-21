import pandas as pd
import numpy as np

def import_excel(file_path):
    '''
    Use r berfore file path e,g. (r'path')
    or use double back slash \\
    '''
    df = pd.read_excel(file_path)
    print("file reading successfull")
    return df

def import_csv(file_path):
    '''
    Use r berfore file path e,g. (r'path')
    or use double back slash \\
    '''
    df = pd.read_csv(file_path)
    return df


def data_frame_info(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input must be a pandas DataFrame.")
    '''
    Input : data farame variable name

    shape return shape of fata frame
    data_type returns data type of each column 
    summary gives statistical overview of data frame
    column_names return name of columns in data frame
    null_values and na_values return count of null and NA values in columns of data frame

    '''
    info = {
        'shape': df.shape,
        
        'data_types': df.dtypes,
        
        'summary': df.describe(),
        
        'column_names': df.columns.tolist(),
        
        'null_values': df.isnull().sum(),
        
        'na_values': df.isna().sum(),
        
        'duplicated_records': df.duplicated().sum()
    }
    
    return info

def print_info(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input must be a pandas DataFrame.")
    info = data_frame_info(df)
    for key, value in info.items():
        print(key)
        print(value,'\n')


