#!/usr/bin/python

import file

result = file.read_csv_to_array('fibonacci.csv')

result = file.convert_array_to_number_array_if_possible(result)

print(result)