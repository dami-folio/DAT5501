# GOAL: plot a histogram of the fraction of votes for a particular candidate for each state in america

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

us_election_data = pd.read_csv("US-2016-primary.csv", delimiter = ";") # the delimiter removes incorrect separators and replaces them with the typical separator
print(us_election_data.info())
