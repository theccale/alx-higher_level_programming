#!/usr/bin/python3
""" A function that defines a Pascal's Triangle """

def pascal_triangle(n):
    """
    Represents a pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triag = triangles[-1]
        tmp = [1]
        for i in range(len(triag) - 1):
            tmp.append(triag[i] + triag[i + 1])
            temp.append(1)
            triangles.append(tmp)
            return triangles
