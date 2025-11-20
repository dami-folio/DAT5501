import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

price_for_light_df = pd.read_csv('price-for-light-uk.csv').drop('Code', axis=1).drop('Entity', axis=1)
price_for_light_df_exclude = price_for_light_df.query('1997 > Year > 1905')
price_for_light_df_include = price_for_light_df.query('2007 > Year > 1905') # dataset up to 2006

x_val = price_for_light_df_exclude['Year']
y_val = price_for_light_df_exclude['Price for Light']

include_x_val = price_for_light_df_include['Year']
include_y_val = price_for_light_df_include['Price for Light']

# polymodel = np.poly1d(np.polyfit(x_val, y_val, 11))
# line = np.linspace(1906, 1996, 100)
# initial_polyfit = np.polyfit(x = price_for_light_df_exclude['Year'], y = price_for_light_df_exclude['Price for Light'], deg = 1)
# plt.scatter(x_val, y_val, marker = 'x', color = '#fa4b91')
# plt.plot(line, polymodel(line), color = '#7d4bfa')
# plt.show()

# making a graph to compare polynomial orders 2 - 20 against the actual data over 90 years

poly_order = 2 # global so that they can be used in other functions
max_poly_order = 15

plt.scatter(x_val, y_val, marker = '.', color = '#fa4b91', s = 5, label = 'Data points')
plt.xlabel('Year')
plt.ylabel('Price for Light (£)')
plt.title(f'Price for Light (UK): 1906 - 1996\n(Polynomial orders: {poly_order} - {max_poly_order})')

chi_squared_orders = []
chi_squared_vals = []
chi_squared_reduced_vals = []


def polynomial_calc():
    global poly_order, max_poly_order
    # line = np.linspace(1906, 1996, 100) # first parameter = starting point, second parameter = ending point, third parameter = sample num to make
    # plt.grid()
    for polynomial in range(poly_order, max_poly_order + 1): # it's max_poly_order + 1 because range does not include the stop value
        # polymodel = np.poly1d(np.polyfit(x_val, y_val, poly_order))
        # plt.plot(line, polymodel(line), lw = 0.6)
        coefficients = np.polyfit(x_val, y_val, poly_order)
        poly = np.poly1d(coefficients)
        plt.plot(x_val, poly(x_val), lw = 0.6)

        residuals = poly - y_val # calculating chi2 within the polynomial function
        chi_squared = 0
        for residual in residuals:
            chi_squared += (residual ** 2)
            dof = len(x_val) - (poly_order + 1)
            chi_squared_reduced = chi_squared / dof
        chi_squared_vals.append(chi_squared)
        chi_squared_orders.append(poly_order)
        chi_squared_reduced_vals.append(chi_squared_reduced)

        poly_order += 1

    plt.show()

def chi_squared_plot():
    plt.plot(chi_squared_orders, chi_squared_reduced_vals, marker = '.')
    plt.show()

polynomial_calc()
print(chi_squared_reduced_vals)
chi_squared_plot()

# def polynomial_func(x_coords, y_coords, degree):
    # coefficients = np.polyfit(x_coords, y_coords, degree)
    # poly = np.poly1d(coefficients)
    # return poly

# polynomial_order_compare()

def chi_squared():
    global poly_order, max_poly_order
    for polynomial in range(poly_order, max_poly_order + 1): # reused from previous function
        coefficients = np.polyfit(x_val, y_val, poly_order)
        poly = np.poly1d(coefficients)
        # chi_squared_val = np.sum((np.polyval(poly, x_val) - y_val) ** 2)
        chi_squared_val = np.sum(price_for_light_df_include) * (((x_val) - ()) ** 2)
        plt.plot(poly_order, chi_squared_val)
        poly_order += 1
    plt.show()

# chi_squared()

# uncertainty = 1
# observed_val = data value
# expected_val = polynomial value
# n = number of data points