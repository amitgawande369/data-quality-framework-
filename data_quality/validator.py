import pandas as pd


class DataQualityValidator:
    """
    A simple data quality framework for validating datasets
    before loading into a database.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def check_missing_values(self) -> pd.Series:
        """Returns count of missing values per column."""
        return self.df.isnull().sum()

    def remove_duplicates(self) -> pd.DataFrame:
        """Removes duplicate rows."""
        self.df = self.df.drop_duplicates()
        return self.df

    def validate_numeric_columns(self, numeric_columns: list) -> pd.DataFrame:
        """
        Ensures numeric columns contain valid numbers.
        Invalid values are converted to NaN.
        """
        for col in numeric_columns:
            self.df[col] = pd.to_numeric(self.df[col], errors="coerce")
        return self.df

    def run_all_checks(self, numeric_columns: list) -> pd.DataFrame:
        """Runs all data quality checks."""
        missing = self.check_missing_values()
        if missing.any():
            print("Missing values detected:")
            print(missing[missing > 0])

        self.remove_duplicates()
        self.validate_numeric_columns(numeric_columns)

        print("Data quality checks completed.")
        return self.df
