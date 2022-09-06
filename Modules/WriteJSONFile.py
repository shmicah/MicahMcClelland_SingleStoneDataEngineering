"""This Module contains a single function (write_json) that takes a JSON formatted string and writes to a .JSON file."""

def write_json(JSONFilePath: str, WriteMode: str, JSONString: str):
    """Takes a JSON string and writes to specified JSON file. User has the option to specify the write operation, where:

    'w' will overwrite the file

    "a" will append to the file
    """
    try:
        with open(JSONFilePath, WriteMode) as outfile:
            outfile.write(JSONString)
    except FileNotFoundError:
        print ("File not found")
    else:
        print("JSON File written successfully to: " + JSONFilePath)

if __name__ == '__main__':
    print("WriteJSONFile is designed as an importable module only.")
else:
    print("WriteJSONFile imported.")
