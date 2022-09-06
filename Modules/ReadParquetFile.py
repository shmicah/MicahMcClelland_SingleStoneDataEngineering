"""This Module contains a single function (get_parquet_data) that loads a parquet file and returns a pandas dataframe."""

import pandas as pd
import sys

def get_parquet_data(ParquetPath: str, ColumnList: list = None):
    """
       Takes a string filepath to a parquet file, returns a Pandas dataframe of the entire file.

       Optional Parameter:
           'ColumnList' - Provide a series of column names to load a subset of the file, otherwise all columns will be read
       """
    try:
        ParquetDataframe = pd.read_parquet(ParquetPath, columns=ColumnList)
        #Do required processing here
        return ParquetDataframe
    except FileNotFoundError as FileException:
        print("File was not found, please check file pathname and format.")
        print(FileException)
        sys.exit(1)
    except TypeError as TypeException:
        print("Type error occurred on function call, please check function call parameters datatypes.")
        print(TypeException)
        sys.exit(1)
    except ValueError as ValueException:
        print("A Value error occurred on function call:")
        print(ValueException)
        sys.exit(1)
    except Exception as GeneralError:
        print("GetParquetData has thrown an exception:")
        print(GeneralError)
        sys.Exit(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("ReadParquetFile is designed as an importable module only.")
else:
    print("ReadParquetFile imported.")
