'''Алгоритмы поиска'''

def linear(val, array):
    '''Линейный поиск'''
    for i, x in enumerate(array):
        if x == val:
            return i
    return -1

def binary(val, array):
    '''Бинарный поиск'''
    low = 0
    high = len(array)-1
    while low <= high:
        m = low + (high-low)//2
        if array[m] == val:
            return m
        elif array[m] < val:
            low = m+1
        else: 
            high = m-1
    return -1

def interpolation(val, array):
    '''Интерполяционный поиск (только для числовых данных)'''
    low = 0
    high = len(array)-1
    while low <= high and val >= array[low] and val <= array[high]:
        m = low + (high-low)*(val-array[low])//(array[high]-array[low])
        if array[m] == val:
            return m
        elif array[m] < val:
            low = m+1
        else: 
            high = m-1
    return -1
