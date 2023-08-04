# data_quality_with_great_expectations
### Introduction
I have tried to create a data quality test project by using great expectations library.

### Description
Below are the details of the folder structure - 
1. config/config.json - It contains the contract of the data product describing each column ingestion & standardization details along with data quality tests details. In this project only using data quality rules. 
2. expectation/Expectation.py - Abstract class for defining an expectation
4. expectation/NotNullExpectation.py - Class inherits Expectation class and implements test function to check for null
5. expectation/UniqueExpectation.py - Class inherits Expectation class and implements test function to check for unique values
6. expectation/ValuesInListExpectation.py - Class inherits Expectation class and implements test function to check if values are within the defined value set
7. utils/utils.py/create_df_from_dq_results - A function to create dataframe out of great expectations validation result
8. reader/JSONFileReader.py - Class to read JSON file and return python dictionary
9. requirements.txt - Contains all the required python packages
10. main.py - A sample run of the framework.

### Steps to run the project
1. Create a python virtual environement -
    `python3 -m venv ./venv`
2. Activate a virtual environment -
   `source ./venv/bin/activate`
3. Install required packages -
    `pip install -r requirements.txt`
4. Run main.py
   `python main.py`
