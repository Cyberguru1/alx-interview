#!/usr/bin/python3
"""Rotating a 2-dimenstional matrix"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """_summary_

    Args:
        matrix (list[list[int]]): input matrix

    Returns: None
    """
    matrix = list(zip(*matrix[::-1]))
