# coding goal: clean NVDA data, then plot closing price against date.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

nvda_data = pd.read_csv("NVDA_hist_price_data.csv", parse_dates = ["Date"]) # import the data using pandas, which is more flexible in recongnising datatypes

# upon import, all columns except for the volume column read as strings due to extra characters present in them.
# the parse_dates parameter combats the dates being misread, but the monetary values have to be separately cleaned.

cols_to_clean = ["Close/Last", "Open", "High", "Low"]
# nvda_data['Open'] = nvda_data['Open'].str.replace('$', '')

def column_cleaning(columns):
    for item in columns: # for each column that needs to be cleaned...
        nvda_data[item] = nvda_data[item].str.replace("$", "") # ...replace any dollar signs with whitespaces.
        nvda_data[item] = nvda_data[item].astype(float)
    return nvda_data

column_cleaning(cols_to_clean)

print(nvda_data.info())

# creating graph of closing prices over the span of a year.

def closing_price_plot(show_graph):
    fig, ax = plt.subplots()

    ax.plot(nvda_data["Date"], nvda_data["Close/Last"], color = "#d92588")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price ($)")
    ax.set_title("NVIDIA Closing Prices")
    if show_graph == True:
        plt.show()
    else:
        pass

# calculate daily change in price, then time how long it takes to sort the differences, for n = 7
# to n = 365. then plot the time against the values of n.

# [nvda_data["Close/Last"][0]]
nvda_daily_price_change = np.array(0.0)

index_point = 0 # aka an iterable index number that moves forward throughout the for-loop to allow for a 
# 'rolling difference' of sorts

for item in nvda_data["Close/Last"]:
    price_change_value = nvda_data['Close/Last'][index_point + 1] - nvda_data['Close/Last'][index_point]
    nvda_daily_price_change = np.append(nvda_daily_price_change, price_change_value)
    index_point += 1
    if index_point == len(nvda_data["Close/Last"]) - 1:
        break

# print(nvda_daily_price_change)

# timing the duration of a simple sort function on the price change data...

# limit = len(nvda_daily_price_change)

start_time = time.time()
nvda_daily_price_change[0:8].sort()
end_time = time.time()
print(f"{(end_time - start_time) * 1000} ms")

# closing_price_plot(False)
# print(nvda_data.head())