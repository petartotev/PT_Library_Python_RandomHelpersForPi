"""
Project is a beginners' guide to manipulating data extracted from .csv files.
.csv file was generated from [AdventureWorks2019].[Person].[Person]
"""

import pandas as pd
import numpy as np


def get_data_from_csv_table():
    """
    Function extracts data from .csv file and prints its statistics.
    """
    data = pd.read_csv("res/adventureworks2019_person_person.csv")
    return data


def print_data_statistics(data):
    print("-" * 100)
    print("data.head():")
    print(data.head())  # First 5 rows + [5 rows x 10 columns]

    print("-" * 100)
    print("data.tail(3):")
    print(data.tail(3))  # Last 3 rows + [3 rows x 10 columns]

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


def generate_data_frame_random():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    return df


def generate_data_custom():
    rows_headings = list("1234567")
    df = pd.DataFrame(np.random.randn(7, 4), index=rows_headings, columns=list("ABCD"))
    return df


def main():
    """
    Function executes main logic of program.
    """
    data = get_data_from_csv_table()
    print_data_statistics(data)

    data_frame_random = generate_data_frame_random()
    print(data_frame_random)

    data_custom = generate_data_custom()
    print(data_custom)
    data_custom.to_csv("res/data_custom_output.csv")
    

if __name__ == "__main__":
    main()
