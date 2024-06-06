# Project: Number Study ; Pascal's Triangle
# Description: This file contains the functions for creating Triangles, Pascal's Triangle, and Simulating Plinko Distribution
# Author: Yarnlet (Zoe S.)
# Last Modified: 2024-06-06

import random
from math import factorial


def construct_triangle(rows: int, placeholder: int) -> list:
    triangle = []

    for n in range(rows):
        row = []

        for k in range(n + 1):
            row.append(placeholder)
        
        triangle.append(row)

    return triangle


def pascal_triangle(rows: int) -> list:
    triangle = []  # create base list

    for n in range(rows):
        row = []  # create base row list

        for k in range(n + 1):
            element = factorial(n) // (factorial(k) * factorial(n - k)) # perform operation
            row.append(element)

        triangle.append(row)

    return triangle # finished triangle (list)


def plinko_simulation(rows: int, runs: int, balls: int = 30) -> list:
    triangles = [] # store all triangles
    total_triangle = construct_triangle(rows, 0)

    for run in range(runs):
        triangle = construct_triangle(rows, 0)
        
        for ball in range(balls):
            ball_shift = 0

            for row in range(rows):

                if row == rows - 1:
                    triangle[row][ball_shift] += 1
                    total_triangle[row][ball_shift] += 1

                ball_shift += random.choice([0, 1]) # 1 is a right path and 0 is a left path

        triangles.append(triangle)
    
    # Calculate the average
    average_triangle = [[cell / runs for cell in row] for row in total_triangle]

    return average_triangle