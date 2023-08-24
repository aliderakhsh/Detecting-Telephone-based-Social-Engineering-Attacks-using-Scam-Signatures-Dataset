import pandas as pd
import math


def load_excels_into_list(num_excels: int, base_path: str) -> list:
    """
  Load multiple Excel files into a list of DataFrames.

  Parameters:
  - num_excels: Number of Excel files to load.
  - base_path: Path template for the Excel files.

  Returns:
  - List of loaded DataFrames.
  """
    excel_list = []
    for i in range(1, num_excels + 1):
        path = f"{base_path}{i}.xlsx"
        df = pd.read_excel(path)
        excel_list.append(df)
    return excel_list


def dataframes_to_lists(dataframes: list) -> list:
    """
  Convert a list of DataFrames to a list of lists.

  Parameters:
  - dataframes: List of DataFrames to convert.

  Returns:
  - List of lists.
  """
    return [df.values.tolist() for df in dataframes]


def extract_columns_from_data(data_list: list, num_cols: int) -> list:
    """
  Extract specific columns from a list of 2D lists.

  Parameters:
  - data_list: List of 2D lists to process.
  - num_cols: Number of columns to extract.

  Returns:
  - List of lists containing extracted columns.
  """
    extracted = []
    for data in data_list:
        columns = [[] for _ in range(num_cols)]
        for row in data:
            for k in range(1, 2 * num_cols, 2):
                if isinstance(row[k], str) or not math.isnan(row[k]):
                    col_idx = k // 2
                    columns[col_idx].append(row[k])
        extracted.append(columns)
    return extracted


# Main script execution
base_path = "SCAM/SCAM_"
num_excels = 5
num_cols = 15

# Load Excel files into a list of DataFrames
excels = load_excels_into_list(num_excels, base_path)

# Convert the DataFrames to lists
excel_lists = dataframes_to_lists(excels)

# Extract specific columns from the data
extracted_columns = extract_columns_from_data(excel_lists, num_cols)

print("Completion Status: The 'extracted_columns' variable contains 15 samples from each of the 5 scam conversation categories.")
