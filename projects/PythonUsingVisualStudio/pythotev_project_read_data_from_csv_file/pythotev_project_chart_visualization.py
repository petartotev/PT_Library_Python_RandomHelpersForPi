"""
This is an experiment with charts.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_lines_from_txt_file():
    """
    Read lines from a .txt file. No module needs to be imported.
    """
    file_t = open("res/data_red_t.txt")
    lines_t = file_t.readlines()
    line_t = lines_t[0]

    file_x = open("res/data_red_x.txt")
    lines_x = file_x.readlines()
    line_x = lines_x[0]

    return line_x, line_t


def visualize_chart_something():
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 6, 9, 10, 9, 8, 6, 7, 4])
    plt.xlabel("x nums")
    plt.ylabel("y nums")
    plt.show()


def visualize_chart_movement_winner_worm_from_txt_files():
    line_x, line_t = read_lines_from_txt_file()
    line_x_split = line_x.split(', ')
    line_t_split = line_t.split(', ')
    print(len(line_x_split))
    print(len(line_t_split))
    line_x_int = list(map(int, line_x_split))
    line_t_float = list(map(float, line_t_split))
    plt.plot(line_x_int, line_t_float)
    plt.xlabel("x nums")
    plt.ylabel("t nums")
    plt.show()


def main():
    visualize_chart_something()
    visualize_chart_movement_winner_worm_from_txt_files()


if __name__ == "__main__":
    main()
