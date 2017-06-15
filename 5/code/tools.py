def trapeze(fnc, start_x, end_x, n):
    result = 0

    delta_x = (end_x - start_x) / n

    i = 0

    xi = start_x + (i * delta_x)

    for i in range(i, n):
        xii = start_x + ((i + 1) * delta_x)

        result += ((fnc(xi) + fnc(xii)) * delta_x) / 2

        xi = xii

    return result


# def simpson(fnc, start_x, end_x, n):
#     h = (end_x - start_x) / n
#
#     k = 0.0
#
#     x = start_x + h
#
#     range_max = int(round(n / 2))
#
#     for i in range(1, range_max + 1):
#         k += 4 * fnc(x)
#         x += 2 * h
#
#     x = start_x + 2 * h
#
#     for i in range(1, range_max):
#         k += 2 * fnc(x)
#         x += 2 * h
#
#     return (h / 3) * (fnc(start_x) + fnc(end_x) + k)


def simpson(fnc, start_x, end_x, n):
    result = fnc(start_x)

    delta_x = (end_x - start_x) / n

    range_max = end_x - delta_x

    x = start_x + delta_x

    while x < range_max:
        result += 4 * fnc(x)
        result += 2 * fnc(x + delta_x)
        x += 2 * delta_x

    result += 4 * fnc(range_max)

    result += fnc(end_x)

    result *= delta_x / 3

    return result
