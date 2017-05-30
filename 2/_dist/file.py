#!/usr/bin/python

import numpy as np


CSV_SEPERATOR = ';'


def read_csv_to_array(filename, csv_seperator=CSV_SEPERATOR):
    file = open(filename, 'r')

    result = []

    for line in file:
        result.append(line.rstrip('\n').split(csv_seperator))

    file.close()

    return result


def convert_value_to_number_if_possible(value):
    if isinstance(value, list):
        return convert_array_to_number_array_if_possible(value)

    if value.isdigit():
        return float(value)

    return value


def convert_array_to_number_array_if_possible(input):
    return list(map(convert_value_to_number_if_possible, input))

def convert_table_data_to_numpy_column_data_array(data_table, remove_head_row = True):
    if remove_head_row:
        data_table = data_table[1:]

    return np.array(data_table).T
