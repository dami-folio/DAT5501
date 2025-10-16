import matplotlib.pyplot as plt
import numpy as np
import random as rd

# random data can be generated using numpy, so i'll define a function to do so. 

gradient = 2.5
intercept = 2

x_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_coords = [2]

print(len(x_coords))

for coord in x_coords:
    if coord == 10:
        break
    else:
        print(coord)
        y_coordinate = ((gradient * x_coords[coord]) + intercept) + rd.random()
        y_coords.append(round(y_coordinate, 1))
        print(y_coordinate, y_coords)

print ("successful!")
