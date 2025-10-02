# acknowledging that y = mx + c, m and c are going to be set values by us.
# y will be allowed to vary from it's exact value on a randomised basis.

import random
import numpy as np

def linear_data_gen(x_start_range, x_end_range, increment_val): # where x allows us to choose a number of values to be generated
    LINEAR_GRADIENT = 2 # set constant
    Y_INTERCEPT = 4 # set constant
    x_axis = []
    x_axis.append(increment_val)
    for value in range(x_start_range, x_end_range): # for each value between the starting and ending point...
        x_value = increment_val + x_axis[-1] # take the last value in the x_axis list and increment it by the outlined value.
        x_axis.append(x_value) # take the new value and append it into the x_axis list.
    y_val_count = len(x_axis) # using the length of this list, the number of y values to be generated is decided.
    y_axis = []
    y_startpoint = random.randint(-10, 10) # a random starting point is also decided for the y_axis.
    y_axis.append(y_startpoint)
    y_endpoint = (LINEAR_GRADIENT * x_axis[-1]) + Y_INTERCEPT
    for point in range(y_startpoint, y_endpoint, y_val_count):
        y_value = (LINEAR_GRADIENT * x_axis[point]) + Y_INTERCEPT
        y_axis.append(y_value)
    random_linear_data = np.savetxt('random_linear_data.csv', [p for p in zip(x_axis, y_axis)])
    return random_linear_data # turn the data into a csv and return it.

linear_data_gen(1, 15, 2)

# INCOMPLETE.