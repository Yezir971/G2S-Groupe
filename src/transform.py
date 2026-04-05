import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime

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
            data_file['nom_candidat'] = "Ahmedaly"
            data_file['date_import'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

def convert_amount(data : pd.DataFrame, columns: list)-> pd.DataFrame:
    """Convert in float the amount

    Args:
        data (pd.DataFrame): DataFrame containing the data to be converted
        columns (list): List of column names to convert to float

    Raises:
        KeyError: If any of the specified columns are not found in the DataFrame

    Returns:
        pd.DataFrame: DataFrame with specified columns converted to float
    """
    # check if the columns is in the data
    # identify all columns 
    missing_collumns = [ element for element in columns if element not in data.columns ]
    if missing_collumns : 
        raise KeyError(f"The following columns are missing or misspelled: {' ,'.join(missing_collumns)}")
    # todo : convert : Base salaire - Taux salire - Montant salarial - Base patronal - Taux patronal - Montant patronal - Montant Total   
    return data.astype({ element : "float64" for element in columns })


def export_to_csv(data: pd.DataFrame, file_name: str) -> None:
    """Export DataFrame to a CSV file

    Args:
        data (pd.DataFrame): DataFrame to be exported
        file_name (str): Name of the output CSV file
    """
    data.to_csv(file_name, index=False)

    
def initialisation():
    """Function for data preparation
    """
    # loading all files in the data directory
    data = loading_file(get_paths("./data"))
    # convert amount to float
    data_convert = convert_amount(data, ['Effectif', 'Bulletin paie', 'Base salariale','Taux salarial', 'Montant salarial', 'Base patronale', 'Taux patronal','Montant patronal', 'Montant total'])
    # check if the Matricule column contains null values
    if is_matricule_null(data) :
        raise ValueError("Null values found in the Matricule column.")
    # convert the data to csv file
    export_to_csv(data_convert, "JDP_Consolide.csv")