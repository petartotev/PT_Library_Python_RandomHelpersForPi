"""
This is an experiment with charts.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 6, 9, 10, 9, 8, 6, 7, 4])
    plt.xlabel('x nums')
    plt.ylabel('y nums')
    plt.show()


if __name__ == "__main__":
    main()
