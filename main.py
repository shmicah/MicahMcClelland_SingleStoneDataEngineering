"""SingleStone Data Engineering Exercise
Author: Micah McClelland
email: micahmcclelland@gmail.com

This script reads two data files and joins them together then outputs as a JSON file.

Please refer to README.md for developer notes and package requirements.
"""

#Import modules and packages
from Modules.ReadCSVFile import get_csv_data
from Modules.ReadParquetFile import get_parquet_data
from Modules.WriteJSONFile import write_json
import sys

#Execute
if __name__ == '__main__':
    try:
        #Specify required columns to improve performance and protect personal data
        TeacherData = get_parquet_data("DataFiles/teachers.parquet", ['id', 'fname', 'lname', 'email', 'cid'])
        StudentData = get_csv_data("DataFiles/students.csv", "_", "id", ['id', 'fname', 'lname', 'email', 'cid'])
        #Rename ambiguous 'id' column present in both files
        TeacherData = TeacherData.rename(columns={'id': 'id_teacher'})
        #Student 'id' field is the index so copy as as a new column and insert into beginning of dataframe to include in JSON output
        id_student = StudentData.index
        StudentData.insert(0, column='id_student', value=id_student)
        #Left Join of Student file to Teacher file using classid ('cid') as Join key, one student can have many or no classes
        JoinedData = StudentData.join(TeacherData.set_index('cid'), on="cid", lsuffix="_student", rsuffix="_teacher")
        #Build JSON string of JoinedData dataframe formatted as records (array of Objects, where id_student = array index)
        JoinedDataJSON = JoinedData.to_json(orient="records")
        #Write JSON string to file, overwrite existing data using 'w' parameter
        write_json("OutputFiles/StudentRecords.json", "w", JoinedDataJSON)
    except Exception as e:
        print("An error has occurred. Please check Error output:")
        print(e)
        sys.exit(1)




