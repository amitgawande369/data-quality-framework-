import pandas as pd
from data_quality.validator import DataQualityValidator

# Load sample sales data
df = pd.read_csv("sample_data/sales_data.csv")

validator = DataQualityValidator(df)

clean_df = validator.run_all_checks(
    numeric_columns=["price", "quantity_sold"]
)

print("\nCleaned Data:")
print(clean_df)
