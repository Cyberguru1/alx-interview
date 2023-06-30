#!/usr/bin/env python
"""
Desc: alx_interview
cyberguru 
"""

def pascal_triangle(n):
    """
    function to return index of triangle

    Args:
        n (int): index of the triangle
    Returns: nth rows of the triangle
    """

    if n <= 0 :
        return []

    rows = [[1]]

    for x in range(n-1):
        next = rows[x]
        new_array = [1]
        for i in range(x):
            new_array.append(next[i] + next[i+1])
        new_array.append(1)
        rows.append(new_array)
    return rows
