#!/usr/bin/python3
'''
Desc: alx_interview on pascal triangle
Author: cyberguru
'''


def pascal_triangle(n):
    '''
    function to return index of triangle
    Args:
        n (int): index of the triangle
    Returns: nth rows of the triangle
    '''

    if type(n) is not int or n <= 0 :
        return []

    rows = [[1]]

    for x in range(n-1):
        prev_array = rows[x]
        new_array = [1]

        for i in range(x):
            new_array.append(prev_array[i] + prev_array[i+1])

        new_array.append(1)
        rows.append(new_array)

    return rows
