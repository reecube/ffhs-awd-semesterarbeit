#!/usr/bin/python

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