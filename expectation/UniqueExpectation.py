from expectation.Expectation import Expectation

class UniqueExpectation(Expectation):
    def __init__(self, column, dimension, add_info = {}):
        super().__init__(column, dimension, add_info)

    def test(self, ge_df):
        ge_df.expect_column_values_to_be_unique(column=self.column,meta = {"dimension": self.dimension})