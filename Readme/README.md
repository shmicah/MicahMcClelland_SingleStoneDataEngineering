## Data Engineering Python Exercise  

Author: Micah McClelland 
Email: micahmcclelland@gmail.com
Submit Date: 9/6/2022 

Overview: 
This Python program reads two data files and joins them together. The resulting joined data is written to a JSON file.

User Instructions:
main.py - execute the top-level application in the root directory
ExecuteTests.py - run Unit and Integration tests to validate application functionality, exists in the /TestFiles/ subfolder

Recommended Python Version:
Python 3.10

External Package Requirements:
Pandas
PyArrow


File Structure:
1) Root Directory - contains main.py script, Dockerfile for containerization, and all required subfolders
2) DataFiles - subfolder containing source data files (CSV and parquet)
3) Modules - subfolder containing python modules imported by main.py
4) OutputFiles - subfolder where resulting JSON file is written
5) ReadMe - subfolder containing the ReadMe
6) TestFiles - subfolder containing all required files and scripts for running Unit and Integration Tests


Open Items:
1) Integration Test needs further development
2) Debug Integration Test not recognized by unittest framework
3) Additional source file data processing could be added, depending on requirements
4) Provide Test Framework execution entry point
5) Force Python3 env for Docker to ensure compatibility moving forward
6) Improve Dockerfile to use Requirements.txt

Assumptions:
1) No checks for duplicates or null entries are made in the file parsing functions. Assumption is 2 valid, complete files are provided
2) JSON File Format output assumes one JSON object per student/teacher/classroom combination. Depending on end-user requirements, I believe one Object per Student with a nested array of JSON Class/Teacher Objects would be most logical structure, but it may not populate into a database easily
3) A Student can have no teacher or assigned class and still be included in the JSON output
