"""
If !this => ERR: "Missing module docstring [C:missing-module-docstring]".
...
'pip install black' => Ctrl + K + D to work as a code beautify formatter.
...
run .py script using command: python pythotev_project_read_data_from_csv_file.py arg01 arg02 arg03
"""

import sys
import datetime


def main():
    """
    If !this => ERR: "Missing function or method docstring [C:missing-function-docstring]".
    """
    print("Hello World!")
    print(datetime.datetime.now())
    if len(sys.argv) >= 1:
        # ERR: "Line too long (103/100) [C:line-too-long]"
        # ERR: "Consider using enumerate instead of iterating with range [C:consider-using-enumerate]"
        # for i in range(0, len(sys.argv)):
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
