#!/usr/bin/python

def check_arrays(results, expected_results, on_function = None):
    if not on_function is None:
        if results == expected_results:
            print('')
            print('[SUCCESS] Die `' + on_function + '`-Funktion funktioniert wie erwartet')
        else:
            print('')
            print('[ERROR] Die `' + on_function + '`-Funktion funktioniert nicht wie erwartet:')
            print('- Erwartet: ' + str(expected_results))
            print('- Erhalten: ' + str(results))
    return results == expected_results