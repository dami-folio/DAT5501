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

poly_order = 3 # global so that they can be used in other functions
max_poly_order = 15

def polynomial_order_compare():
    global poly_order
    global max_poly_order
    # line = np.linspace(1906, 1996, 100) # first parameter = starting point, second parameter = ending point, third parameter = sample num to make
    plt.scatter(x_val, y_val, marker = '.', color = '#fa4b91', s = 5, label = 'Data points')
    # plt.grid()
    plt.xlabel('Year')
    plt.ylabel('Price for Light (£)')
    plt.title(f'Price for Light (UK): 1906 - 1996\n(Polynomial orders: {poly_order} - {max_poly_order})')
    for polynomial in range(poly_order, max_poly_order + 1): # it's max_poly_order + 1 because range does not include the stop value
        # polymodel = np.poly1d(np.polyfit(x_val, y_val, poly_order))
        # plt.plot(line, polymodel(line), lw = 0.6)
        coefficients = np.polyfit(x_val, y_val, poly_order)
        poly = np.poly1d(coefficients)
        plt.plot(x_val, poly(x_val), label = f'Poly. order: {poly_order}', lw = 0.6)
        poly_order += 1
    plt.legend()
    plt.show()

polynomial_order_compare()

def chi_squared(df, column):
    # (sum of data points) * ((observed_val - expected_val)**2) / (uncertainty)**2
    observed_val = None
    expected_val = sum(df[column])
    uncertainty = None
    num_data_points = len(df)

    chi2 = (num_data_points) * ((observed_val - expected_val)**2) / (uncertainty)**2
    return chi2