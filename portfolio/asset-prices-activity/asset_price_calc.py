# coding goal: clean NVDA data, then plot closing price against date.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nvda_data = pd.read_csv("NVDA_hist_price_data.csv") # import the data using pandas, which is more flexible in recongnising datatypes

