# coding=utf-8

##########
# 
# Erstellen Sie eine Beispielsammlung von verschiedenen Arten von Graphiken mit Matplotlib;
#   es sollte je ein Beispiel der folgenden Diagrammtypen berücksichtigt werden:
# 
# Funktionsgraphen, 
# Mehrere Funktionsgraphen in der selben Graphik
# Balkendiagramme,
# Tortendiagramme,
# Histogramme.
# Beschreiben Sie jeweils, wie die Diagramme erzeugt werden.
# 
# Stellen Sie dabei auch Daten dar, die Sie von CSV-Dateien eingelesen haben.
# 
##########

import matplotlib.pyplot as plt
import numpy as np

import file

OUTPUT_TYPES = ['1', '2', '3', '4', '5']

# Read fibonacci-data from file
dataTable = file.read_csv_to_array('fibonacci.csv')

# Convert to number array
dataTable = file.convert_array_to_number_array_if_possible(dataTable)

# Remove heading row of table-data and convert it to numpy-column-data-array
dataGraph = file.convert_table_data_to_numpy_column_data_array(dataTable)

# Show valid output types
print('')
print('Ausgabetypen:')
print('-------------')
print('`' + OUTPUT_TYPES[0] + '`: Funktionsgraphen')
print('`' + OUTPUT_TYPES[1] + '`: Mehrere Funktionsgraphen in der selben Graphik')
print('`' + OUTPUT_TYPES[2] + '`: Balkendiagramme')
print('`' + OUTPUT_TYPES[3] + '`: Tortendiagramme')
print('`' + OUTPUT_TYPES[4] + '`: Histogramme')
print('')

# Ask the user for an output type
outputType = input('Bitte wählen Sie einen Ausgabetypen: ')

# ###########################################################################
# Funktionsgraphen
if outputType == OUTPUT_TYPES[0]:
    # Set the graph title
    plt.title('Funktionsgraphen')

    # Prepare the graph-data
    plt.plot(dataGraph[0], dataGraph[1], linestyle='dashed', marker='o', color='green')

    # Show the graph
    plt.show()

# ###########################################################################
# Mehrere Funktionsgraphen in der selben Graphik
elif outputType == OUTPUT_TYPES[1]:
    # Set the graph title
    plt.title('Mehrere Funktionsgraphen in der selben Graphik')

    # Prepare the graph-data
    plt.plot(dataGraph[0], dataGraph[1], 'ro--', dataGraph[0], dataGraph[2], 'b^--')

    # Show the graph
    plt.show()

# ###########################################################################
# Balkendiagramme
elif outputType == OUTPUT_TYPES[2]:
    # Set the graph title
    plt.title('Balkendiagramme')

    # Prepare the graph-data
    plt.bar(dataGraph[0], dataGraph[1], color='green')

    # Show the graph
    plt.show()

# ###########################################################################
# Tortendiagramme
elif outputType == OUTPUT_TYPES[3]:
    # Set the graph title
    plt.title('Tortendiagramme')

    # Custom values and labels
    values = [13, 7, 25, 2, 2]
    labels = ['Bern', 'Freiburg', 'Zürich', 'Genf', 'Uri']

    # Prepare the graph-data
    plt.pie(values, labels=labels, startangle=90)

    # Show the graph
    plt.show()

# ###########################################################################
# Histogramme
elif outputType == OUTPUT_TYPES[4]:
    # Set the graph title
    plt.title('Histogramme')

    # Prepare the graph-data
    x = np.random.normal(size=1000)
    plt.hist(x, normed=True, bins=30, color='green')

    # Show the graph
    plt.show()

# ###########################################################################
# Invalid
else:
    print('Der Ausgabetyp `' + outputType + '` ist ungültig!')
