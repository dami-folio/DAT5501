import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

price_for_light_df = pd.read_csv('price-for-light-uk.csv').drop('Code', axis=1).drop('Entity', axis=1)
price_for_light_df_exclude = price_for_light_df.query('1997 > Year > 1905')

x_val = price_for_light_df_exclude['Year']
y_val = price_for_light_df_exclude['Price for Light']

polymodel = np.poly1d(np.polyfit(x_val, y_val, 11))
line = np.linspace(1906, 1996, 100)
# initial_polyfit = np.polyfit(x = price_for_light_df_exclude['Year'], y = price_for_light_df_exclude['Price for Light'], deg = 1)
plt.scatter(x_val, y_val, marker = 'x', color = '#fa4b91')
plt.plot(line, polymodel(line), color = '#7d4bfa')
plt.show()
print(price_for_light_df_exclude)


