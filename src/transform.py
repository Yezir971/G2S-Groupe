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
        return pd.concat(all_data_file)
    else:
        print("No Excel files found in the specified directory.")
        return pd.DataFrame()




def test():
    """Function testing
    """
    print("This is a test function")
    loading_file(get_paths("./data"))