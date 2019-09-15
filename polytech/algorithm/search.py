"""Алгоритмы поиска"""

# Линейный поиск
def linear(val, array):
    for i, x in enumerate(array):
        if x == val:
            return i
    return -1
