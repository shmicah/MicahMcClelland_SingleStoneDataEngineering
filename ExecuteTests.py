import unittest
import json
from Modules.ReadCSVFile import get_csv_data
from Modules.ReadParquetFile import get_parquet_data
from Modules.WriteJSONFile import write_json


class DataEngineeringExercise_TestSuite(unittest.TestCase):
    """Unit Tests to confirm that file read functions work; Integration Test to confirm file read > processing > file write maintains data integrity"""
    def test_get_csv_data(self):
        csv_test_data = get_csv_data("TestFiles/TestData/test_csv_data.csv", "_")
        #Test column values parsed correctly
        self.assertEqual(csv_test_data["CSV_ColumnB"][0], "Bar")
        self.assertEqual(csv_test_data["CSV_ColumnA"][0], "Foo")
        #Test resulting dataframe column count and size correct
        self.assertEqual(len(csv_test_data.columns), 2)
        #2 columns * 1 row = size(2)
        self.assertEqual(csv_test_data.size, 2, "CSV function failed")
        print("CSV Test Completed")
    def test_get_parquet_data(self):
        #reusing existing parquet file to save myself time, should use control data instead
        parquet_test_data = get_parquet_data("TestFiles/TestData/test_parquet_data.parquet", ["id", "fname"])
        # Test column values parsed correctly
        self.assertEqual(parquet_test_data['id'][0], "51-3016916")
        # Test resulting dataframe column count and size correct
        self.assertEqual(len(parquet_test_data.columns), 2)
        #2 columns * 10 rows = size(20)
        self.assertEqual(parquet_test_data.size, 20, "Parquet function failed")
        print("Parquet Test Completed")
    def integration_test(self):
        # This function not being picked up by application?
        # Not a natural place to force integration test... I would prefer to separate it out as its own script
        # This test is not valid - it does not properly compare source data to output, instead it tests returned data against recreation of source
        # It should be comparing two variables directly, which means I should rebuild the json_data_returned back into CSV dataframe format
        # ...but it tests ability of program to read a CSV file into memory and produce a JSON file while maintaing data integrity
        # Test Plan: Read a CSV file, format and write to JSON file, read JSON file back, compare results to original CSV data
        integration_test_data_source = get_csv_data("TestFiles/TestData/test_csv_data.csv", "_")
        integration_test_data = integration_test_data_source.to_json(orient="records")
        write_json("TestFiles/TestData/json_test_data.json", "w", integration_test_data)
        datafile=open("TestFiles/TestData/json_test_data.json")
        json_data_returned = json.load(datafile)
        self.assertEqual(json_data_returned, [{'CSV_ColumnA': 'Foo', 'CSV_ColumnB': 'Bar'}], "Integration test failed")
        datafile.close()
        print("Integration Test Completed")
if __name__ == '__main__':
    unittest.main()