import pandas as pd
from data_quality.validator import DataQualityValidator


def test_missing_values():
    df = pd.DataFrame({
        "price": [100, None],
        "quantity_sold": [10, 20]
    })
    validator = DataQualityValidator(df)
    missing = validator.check_missing_values()
    assert missing["price"] == 1


def test_remove_duplicates():
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "value": [10, 10, 20]
    })
    validator = DataQualityValidator(df)
    cleaned = validator.remove_duplicates()
    assert len(cleaned) == 2


def test_numeric_validation():
    df = pd.DataFrame({
        "price": ["100", "invalid"]
    })
    validator = DataQualityValidator(df)
    cleaned = validator.validate_numeric_columns(["price"])
    assert cleaned["price"].isnull().sum() == 1
