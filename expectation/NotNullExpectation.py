from expectation.Expectation import Expectation

class NotNullExpectation(Expectation):
    def __init__(self, column, dimension, add_info = {}):
        super().__init__(column, dimension, add_info)

    def test(self, ge_df):
        ge_df.expect_column_values_to_not_be_null(column=self.column,meta = {"dimension": self.dimension})