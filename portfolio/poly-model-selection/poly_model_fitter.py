import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy

price_for_light_df = pd.read_csv('price-for-light-uk.csv').drop('Code', axis=1).drop('Entity', axis=1)
price_for_light_df_exclude = price_for_light_df.query('1997 > Year > 1905')

x_val = price_for_light_df_exclude['Year']
y_val = price_for_light_df_exclude['Price for Light']

# polymodel = np.poly1d(np.polyfit(x_val, y_val, 11))
# line = np.linspace(1906, 1996, 100)
# initial_polyfit = np.polyfit(x = price_for_light_df_exclude['Year'], y = price_for_light_df_exclude['Price for Light'], deg = 1)
# plt.scatter(x_val, y_val, marker = 'x', color = '#fa4b91')
# plt.plot(line, polymodel(line), color = '#7d4bfa')
# plt.show()

# making a graph to compare polynomial orders 2 - 20 against the actual data over 90 years

def polynomial_order_compare():
    poly_order = 2
    max_poly_order = 20
    line = np.linspace(1906, 1996, 100) # first parameter = starting point, second parameter = ending point, third parameter = sample num to make
    plt.scatter(x_val, y_val, marker = '.', color = '#fa4b91', s = 5)
    plt.grid()
    plt.xlabel('Year')
    plt.ylabel('Price for Light (£)')
    plt.title('Price for Light (UK): 1906 - 1996\n(Polynomial orders: 2 - 20)')
    for polynomial in range(poly_order, max_poly_order + 1): # it's max_poly_order + 1 because range does not include the stop value
        polymodel = np.poly1d(np.polyfit(x_val, y_val, poly_order))
        plt.plot(line, polymodel(line), lw = 0.5)
        poly_order += 1
    plt.show()

polynomial_order_compare()

# print(price_for_light_df_exclude)