import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np

# the below code formats the 'year' column to be read as a year rather than a number by the analysis modules.
retirement_age_df = pd.read_csv('retirement_age_men_and_women.csv', parse_dates = ['Year'])

# pd.DataFrame() is used to turn the slices into separate dataframes. if this isn't done, then every operation involving
# the sliced dfs will come with the same warning. this might also solve the issue of not being able to join
# the new 'OECD average retirement age' column to the other dfs.

oecd_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'OECD'])
japan_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'Japan'])
s_korea_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'South Korea'])
oecd_df['OECD average retirement age'] = (oecd_df['Average retirement age: Women']+ oecd_df['Average retirement age: Men']) / 2

def column_dropper(dataframe): # quick code to remove the unnecessary columns from the OECD dataframe. functions are fun!
    droplist = ['Entity', 'Code', 'Average retirement age: Women', 'Average retirement age: Men']
    for column in droplist:
        dataframe = dataframe.drop(column, axis=1)
    return dataframe

oecd_df = column_dropper(oecd_df) # set oecd_df's value to the dropped version, in which it only holds the year and 
# average retirement age columns. 

japan_df = pd.merge(japan_df, oecd_df, on='Year') # use pd.merge to join japan_df to oecd_df by the year column.
s_korea_df = pd.merge(s_korea_df, oecd_df, on='Year')

# making new graphs using the new dataframes.

japan_vs_oecd_graph = japan_df.plot(kind = 'line', x = 'Year', 
                               y = ['Average retirement age: Women', 'Average retirement age: Men', 'OECD average retirement age'], 
                               ylabel = 'Average retirement age: Japan vs OECD', 
                               legend = True, title = "Average retirement age: Japan vs OECD average")

japan_vs_oecd_figure = japan_vs_oecd_graph.get_figure()
japan_vs_oecd_figure.savefig("japan_vs_oecd_fig.png")

s_korea_vs_oecd_graph = s_korea_df.plot(kind = 'line', x = 'Year', 
                               y = ['Average retirement age: Women', 'Average retirement age: Men', 'OECD average retirement age'], 
                               ylabel = 'Average retirement age: South Korea vs OECD', 
                               legend = True, title = "Average retirement age: South Korea vs OECD average")

s_korea_vs_oecd_figure = s_korea_vs_oecd_graph.get_figure()
s_korea_vs_oecd_figure.savefig("s_korea_vs_oecd_fig.png")