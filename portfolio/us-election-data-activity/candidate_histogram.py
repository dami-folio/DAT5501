# GOAL: plot a histogram of the fraction of votes for a particular candidate for each state in america

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

us_election_data = pd.read_csv("US-2016-primary.csv", delimiter = ";") # the delimiter removes incorrect separators and replaces them with the typical separator
unwanted_cols = ["fips"]
us_election_data = us_election_data.drop(columns = unwanted_cols)
print(us_election_data.info())

# chosen candidate: bernie sanders.
# make a new dataframe in which solely bernie sanders's election info is present

sanders_df = pd.DataFrame(us_election_data.loc[us_election_data['candidate'] == 'Bernie Sanders'])
print(sanders_df.head())