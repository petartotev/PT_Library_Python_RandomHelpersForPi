"""
Project is a beginners' guide to manipulating data extracted from .csv files.
.csv file was generated from [AdventureWorks2019].[Person].[Person]
"""

import pandas as pd


def get_data_from_csv_table():
    """
    Function extracts data from .csv file and prints its statistics.
    """
    data = pd.read_csv("res/adventureworks2019_person_person.csv")

    print("-" * 100)
    print("data.head():")
    print(data.head())  # First 5 rows + [5 rows x 10 columns]
    print("-" * 100)
    print("data.shape:")  # (25, 10)
    print(data.shape)
    print("-" * 100)
    print("data.describe():")
    print(data.describe())
    print("-" * 100)
    print("data.isnull().sum():")
    print(data.isnull().sum())
    print("-" * 100)
    print("data.dtypes:")
    print(data.dtypes)
    print("-" * 100)


def main():
    """
    If !this => "Missing function or method docstring [C:missing-function-docstring]".
    """
    get_data_from_csv_table()


if __name__ == "__main__":
    main()
