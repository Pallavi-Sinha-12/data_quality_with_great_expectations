def create_df_from_dq_results(spark, dq_results):
    dq_data = []
    for result in dq_results["results"]:
        if result["success"] == True:
            status = 'PASSED'
        else:
            status = 'FAILED'
        dq_data.append((
        result["expectation_config"]["kwargs"]["column"],
        result["expectation_config"]["meta"]["dimension"],
        status,
        result["expectation_config"]["expectation_type"],
        result["result"]["unexpected_count"],
        result["result"]["element_count"],
        result["result"]["unexpected_percent"],
        float(100-result["result"]["unexpected_percent"])
        ))
    dq_columns = ["column", "dimension", "status", "expectation_type", "unexpected_count", "element_count", "unexpected_percent", "percent"]
    dq_df = spark.createDataFrame(data=dq_data,schema=dq_columns)
    return dq_df