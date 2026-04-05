import numpy as np
import pandas as pd
from pathlib import Path

def get_paths(folder_path: str) -> list:
    """Get path for all files in data
    
    Args:
        folder_path (str): path to the data directory
        
    Returns:
        list: A list of paths to the Excel files in the data directory
    """
    dir_path = Path(folder_path)
    files = list(dir_path.glob("*.xlsx"))
    return files


def loading_file(data : list) -> pd.DataFrame:
    """Load data from a list of Excel files
    
    Args:
        data (list): A list of paths to the Excel files
        
    Returns:
        pd.DataFrame: A DataFrame containing the concatenated data from all files
    """
    all_data_file = []
    for file in data: 
        if str(file).endswith('.xlsx'):
            print(f'load file {file}')
            data_file = pd.read_excel(file)
            data_file['source_fichier'] = Path(file).name
            all_data_file.append(data_file)
    if all_data_file: 
        print(all_data_file)
        return pd.concat(all_data_file)
    else:
        print("No Excel files found in the specified directory.")
        return pd.DataFrame()

def is_matricule_null(data: pd.DataFrame)-> bool:
    """_summary_

    Args:
        data (pd.DataFrame): dataframe to check for null values in the Matricule column

    Returns:
        bool: True or false if the Matricule is null
    """
    if data['Matricule'].isna().any():
        return True
    return False




def test():
    """Function testing
    """
    print("This is a test function")
    data = loading_file(get_paths("./data"))
    print(data)
    result = is_matricule_null(data)
    print(result)