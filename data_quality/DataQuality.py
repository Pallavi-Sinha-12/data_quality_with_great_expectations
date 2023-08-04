from reader.JSONFileReader import JSONFileReader
from great_expectations.dataset.sparkdf_dataset import SparkDFDataset
from expectation.NotNullExpectation import NotNullExpectation
from expectation.UniqueExpectation import UniqueExpectation
from expectation.ValuesInListExpectation import ValuesInListExpectation

class DataQuality:

    def __init__(self, pyspark_df, config_path):
        self.pyspark_df = pyspark_df
        self.config_path = config_path

    def rule_mapping(self, dq_rule):
        return{"check_null" : "NotNullExpectation", "check_unique" : "UniqueExpectation", "check_if_values_in_list" : "ValuesInListExpectation"}[dq_rule]

    def _get_expectation(self):
        class_obj = globals()[self.rule_mapping()]
        return class_obj(self.extractor_args)
    
    def convert_to_ge_df(self):
        return SparkDFDataset(self.pyspark_df)
    
    def read_config(self):
        json_reader = JSONFileReader(self.config_path)
        return json_reader.read()
      
    def run_test(self):
        ge_df = self.convert_to_ge_df()
        config = self.read_config()
        for column in config["columns"]:
            for dq_rule in column["dq_rule(s)"]:
                rule_name = dq_rule["rule_name"]
                print(rule_name)
                # get a class object
                expectation_obj = globals()[self.rule_mapping(dq_rule["rule_name"])]
                print(column["src_column"], dq_rule["rule_dimension"], dq_rule["add_info"], rule_name)
                expectation_instance = expectation_obj(column["src_column"], dq_rule["rule_dimension"], dq_rule["add_info"])
                expectation_instance.test(ge_df)

        dq_results = ge_df.validate()
        return dq_results
        



    

    