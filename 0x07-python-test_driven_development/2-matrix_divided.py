#!/usr/bin/python3
"""
Defines a function that divides all elemnts of a matrix
"""

def matrix_divided(matrix, div):
    if type(matrix) != list or any(isinstance(i, list) for i in matrix)is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if isinstance(j, int) is False and isinstance(j, float) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lst = iter(matrix)
    length = len(next(lst))
    if not all(len(i) == length for i in lst):
        raise TypeError("Each row of the matrix must have the same size")
    
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            val = round((j / div), 2)
            row.append(val)
        new_matrix.append(row)

    return new_matrix

# print(matrix_divided([[1, 2, 3], [4, 5, 6]], 0))