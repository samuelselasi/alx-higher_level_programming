#!/usr/bin/python3
"""6. Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elem in m_a:
        if not isinstance(elem, list):
            raise TypeError("m_a must be a list of lists")

    for elem in m_b:
        if not isinstance(elem, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elem in lists:
            if not type(elem) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elem in lists:
            if not type(elem) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    m_len = 0
    for elem in m_a:
        if m_len != 0 and m_len != len(elem):
            raise TypeError("each row of m_a must be of the same size")
        m_len = len(elem)

    m_len = 0
    for elem in m_b:
        if m_len != 0 and m_len != len(elem):
            raise TypeError("each row of m_b must be of the same size")
        m_len = len(elem)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_1 = []
    index_1 = 0

    for elem in m_a:
        row_2 = []
        index_2 = 0
        num = 0

        while (index_2 < len(m_b[0])):
            num += elem[index_1] * m_b[index_1][index_2]

            if index_1 == len(m_b) - 1:
                index_1 = 0
                index_2 += 1
                row_2.append(num)
                num = 0

            else:
                index_1 += 1

        row_1.append(row_2)

    return row_1
