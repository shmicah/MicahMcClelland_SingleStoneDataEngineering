"""This Module contains a single function (get_csv_data) that loads a CSV file and returns a pandas dataframe."""

import pandas as pd
import sys
def get_csv_data(CSVPath: str, FileDelimiter: str, IndexColumnName: str=None, ColumnList: list=None):
    """
    Takes a string filepath to a CSV file and the required delimiter, returns a Pandas dataframe of the entire file.

    Optional Parameters:
        'IndexColumnName' - set column name to be used as index, otherwise Pandas uses first column

        'ColumnList' - Provide a series of column names to load a subset of the file, otherwise all columns will be read
    """
#    assert isinstance (FileDelimiter, str), 'GetCSVData Error: Provided Delimiter must be a string'
    try:
        CSVDataframe = pd.read_csv(CSVPath, delimiter=FileDelimiter, index_col=IndexColumnName, usecols=ColumnList)
        #Do required dataframe processing here
        return CSVDataframe
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
        print("GetCSVData has thrown an exception:")
        print(GeneralError)
        sys.exit(1)

if __name__ == '__main__':
    print("ReadCSVFile is designed as an importable module only.")
else:
    print("ReadCSVFile imported.")
