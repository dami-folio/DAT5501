import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mock_data = pd.read_csv('mock_csv.csv')

def plotter(data):
    return plt.plot(data)

plotted_mock = plotter(mock_data)
plotted_mock.get_figure()