# coding goal: clean NVDA data, then plot closing price against date.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nvda_data = pd.read_csv("NVDA_hist_price_data.csv", parse_dates = ["Date"]) # import the data using pandas, which is more flexible in recongnising datatypes

# upon import, all columns except for the volume column read as strings due to extra characters present in them.
# the parse_dates parameter combats the dates being misread, but the monetary values have to be separately cleaned.

cols_to_clean = ["Close/Last", "Open", "High", "Low"]
# nvda_data['Open'] = nvda_data['Open'].str.replace('$', '')

def column_cleaning(columns):
    for item in columns: # for each column that needs to be cleaned...
        nvda_data[item] = nvda_data[item].str.replace("$", "") # ...replace any dollar signs with whitespaces.
    return nvda_data

column_cleaning(cols_to_clean)

print(nvda_data.info())

# creating graph of closing prices over the span of a year.

# fig, ax = plt.subplots()

# ax.plot(nvda_data["Date"], nvda_data["Close/Last"], color = "#d92588")
# ax.set_xlabel("Date")
# ax.set_ylabel("Closing Price")
# ax.set_title("NVIDIA Closing Prices")
# plt.show()

# print(nvda_data.head())