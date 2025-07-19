import pandas as pd
import os
from IPython.display import display

csv_file_path = "./data/customers-100.csv"

def readFromCSV():
    """
    The purpose of the function is to read from a csv file
    """
    
    if os.path.exists(csv_file_path):
        print(f"File path  {csv_file_path} exists")
        data_df = pd.read_csv(csv_file_path)
        print("first ten rows")
        display(data_df.head(10))
        print("last ten rows")
        display(data_df.tail(10))
    else:
        print(f"File path  {csv_file_path} does not exist")

if __name__ == "__main__":
    readFromCSV()
    