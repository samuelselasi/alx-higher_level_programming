#!/usr/bin/python3i
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    pas_triangles = [[1]]
    while len(pas_triangles) != n:
        triangle = pas_triangles[-1]
        tmp_triangle = [1]

        for i in range(len(triangle) - 1):
            tmp_triangle.append(triangle[i] + triangle[i + 1])

        tmp_triangle.append(1)
        pas_triangles.append(tmp_triangle)

    return (pas_triangles)
