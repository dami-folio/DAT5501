import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

price_for_light_df = pd.read_csv('price-for-light-uk.csv').drop('Code', axis=1).drop('Entity', axis=1)
price_for_light_df_exclude = price_for_light_df.query('1996 > Year > 1905')

initial_polyfit = np.polyfit(x = price_for_light_df_exclude['Year'], y = price_for_light_df_exclude['Price for Light'], deg = 1)
plt.scatter(x = price_for_light_df_exclude['Year'], y = price_for_light_df_exclude['Price for Light'], marker = '.')
plt.show()
