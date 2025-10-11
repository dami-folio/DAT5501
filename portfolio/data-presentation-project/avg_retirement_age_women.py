import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np

# the below code formats the 'year' column to be read as a year rather than a number by the analysis modules.
retirement_age_df = pd.read_csv('retirement_age_men_and_women.csv', parse_dates = ['Year'])

print(type(retirement_age_df['Year'][0])) # quickly checking that parsing the dates changed the data type properly.

