import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

price_for_light_df = pd.read_csv('price-for-light-uk.csv').drop('Code', axis=1).drop('Entity', axis=1)
price_for_light_df = price_for_light_df.query('Year > 1905')


