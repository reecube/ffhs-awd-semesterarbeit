#!/usr/bin/python

import time


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# noinspection PyUnresolvedReferences
def fib_count(n):
    if n < 2:
        return [n, 1]
    else:
        fib1 = fib_count(n - 1)
        fib2 = fib_count(n - 2)
        return [fib1[0] + fib2[0], 1 + fib1[1] + fib2[1]]


def fib_time(n):
    time_before = time.time()
    fib_result = fib(n)
    time_after = time.time()

    time_diff = time_after - time_before

    # Convert: seconds given, returns ms
    time_diff = time_diff * 1000

    return [fib_result, time_diff]


def fib_fast_recursive(n, a=1, b=1):
    n -= 1

    if n <= 0:
        return a

    a, b = b, a + b

    return fib_fast_recursive(n, a, b)


def fib_fast_iterative(n):
    a, b = 1, 1

    for i in range(1, n):
        a, b = b, a + b

    return a


def fib_fast_recursive_time(n):
    time_before = time.time()
    fib_result = fib_fast_recursive(n)
    time_after = time.time()

    time_diff = time_after - time_before

    # Convert: seconds given, returns ms
    time_diff = time_diff * 1000

    return [fib_result, time_diff]


def fib_fast_iterative_time(n):
    time_before = time.time()
    fib_result = fib_fast_iterative(n)
    time_after = time.time()

    time_diff = time_after - time_before

    # Convert: seconds given, returns ms
    time_diff = time_diff * 1000

    return [fib_result, time_diff]
