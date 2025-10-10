# GOAL: import retirement age csv.

import pandas as pd

retirement_age_df = pd.read_csv('retirement_age_men_and_women.csv')
print(retirement_age_df.head)

