#!/usr/bin/python

import fibonacci
import tools

######################################################
# Aufgabe 0                                          #
#                                                    #
# Implementieren Sie eine Python-Funktion fib(n) ,   #
# die die n-te Fibonacci-Zahl bestimmt.              #
######################################################

results = []
expectedResults = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

for i in range(1, len(expectedResults) + 1):
    results.append(fibonacci.fib(i))

tools.check_arrays(results, expectedResults, 'fibonacci.fib')

######################################################
# Aufgabe 1                                          #
#                                                    #
# Eine naive Implementierung setzt die obige         #
# Rekursionsgleichung direkt um. Schreiben Sie eine  #
# weitere Python-Funktion, die berechnet, wie viele  #
# Funktionsaufrufe on fib notwendig sind, um die     #
# n-te Fibonacci-Zahl zu berechnen.                  #
######################################################

countResults = []
expectedCountResults = [[1, 1], [1, 3], [2, 5], [3, 9], [5, 15]]
for i in range(1, len(expectedCountResults) + 1):
    countResults.append(fibonacci.fib_count(i))

tools.check_arrays(countResults, expectedCountResults, 'fibonacci.fib_count')


######################################################
# Aufgabe 2                                          #
#                                                    #
# Vergleichen Sie die Anzahl der Funktionsaufrufe    #
# von fib zur Bestimmung einer Fibonacci-Zahl mit    #
# den Fibonacci-Zahlen selber.                       #
# Koennen Sie eine Vermutung aufstellen?             #
######################################################

countResults = []
for i in range(1, 20 + 1):
    countResults.append(fibonacci.fib_count(i))

print('')
print('[INFO] `fibonacci.fib_count`' + str(countResults))

# TODO: Supply this with a graph


######################################################
# Aufgabe 3                                          #
#                                                    #
# Verwenden Sie die Funktion time() aus dem Modul    #
# time, um zu bestimmen, wie lange die Funktion fib  #
# benoetigt, um eine Fibonacci-Zahl zu bestimmen.    #
######################################################

def print_time(n):
    fib_time = fibonacci.fib_time(n)
    print('[INFO] Die `fibonacci.fib`-Funktion fuer die Zahl `' + str(n) + '` benoetigte `' +
          str(round(fib_time[1], 2)) + '` ms fuer die Durchfuehrung. Resultat: ' + str(fib_time[0]))

print('')
print_time(10)
print_time(20)
print_time(25)
print_time(30)
print_time(31)
print_time(32)


######################################################
# Aufgabe 4                                          #
#                                                    #
# Implementieren Sie eine weitere Python-Funktion    #
# zur Berechnung der n-ten Fibonacci-Zahl, die       #
# moeglichst effizient ist. (Hinweis: das kann       #
# rekursiv oder iterativ geloest werden.)            #
######################################################

def print_fast_recursive_time(n):
    fib_time = fibonacci.fib_fast_recursive_time(n)
    print('[INFO] Die `fibonacci.fib_fast_recursive`-Funktion fuer die Zahl `' + str(n) + '` benoetigte `' +
          str(round(fib_time[1], 2)) + '` ms fuer die Durchfuehrung. Resultat: ' + str(fib_time[0]))

print('')
print_fast_recursive_time(10)
print_fast_recursive_time(20)
print_fast_recursive_time(30)
print_fast_recursive_time(100)
print_fast_recursive_time(200)
print_fast_recursive_time(500)


def print_fast_riterative_time(n):
    fib_time = fibonacci.fib_fast_iterative_time(n)
    print('[INFO] Die `fibonacci.fib_fast_iterative`-Funktion fuer die Zahl `' + str(n) + '` benoetigte `' +
          str(round(fib_time[1], 2)) + '` ms fuer die Durchfuehrung. Resultat: ' + str(fib_time[0]))

print('')
print_fast_riterative_time(10)
print_fast_riterative_time(20)
print_fast_riterative_time(30)
print_fast_riterative_time(100)
print_fast_riterative_time(200)
print_fast_riterative_time(500)
