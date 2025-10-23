# coding goal: clean NVDA data, then plot closing price against date.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nvda_data = pd.read_csv("NVDA_hist_price_data.csv", parse_dates = ["Date"]) # import the data using pandas, which is more flexible in recongnising datatypes

# upon import, all columns except for the volume column read as strings due to extra characters present in them.
# the parse_dates parameter combats the dates being misread, but the monetary values have to be separately cleaned.

cols_to_clean = ["Close/Last", "Open", "High", "Low"]

nvda_data = nvda_data.replace("$", "", regex = True)
print(nvda_data)