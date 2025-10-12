import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np

# the below code formats the 'year' column to be read as a year rather than a number by the analysis modules.
retirement_age_df = pd.read_csv('retirement_age_men_and_women.csv', parse_dates = ['Year'])

# print(type(retirement_age_df['Year'][0])) # quickly checking that parsing the dates changed the data type properly.

# create a mask for the df and apply it to the main csv.

'''
oecd_mask = retirement_age_df['Entity'] == 'OECD'
oecd_df = retirement_age_df[oecd_mask]
japan_mask = retirement_age_df['Entity'] == 'Japan'
japan_df = retirement_age_df[japan_mask]
s_korea_mask = retirement_age_df['Entity'] == 'South Korea'
s_korea_df = retirement_age_df[s_korea_mask] # using a function would be easier, but i think it'd need
# new variables for it to work. i'll look into it later. 
'''

# pd.DataFrame() is used to turn the slices into separate dataframes. if this isn't done, then every operation involving
# the sliced dfs will come with the same warning. this might also solve the issue of not being able to join
# the new 'OECD average retirement age' column to the other dfs.

oecd_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'OECD'])
japan_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'Japan'])
s_korea_df = pd.DataFrame(retirement_age_df.loc[retirement_age_df['Entity'] == 'South Korea'])
oecd_df['OECD average retirement age'] = (oecd_df['Women_avg_retirement_age']+ oecd_df['Men_avg_retirement_age']) / 2

def column_dropper(dataframe): # quick code to remove the unnecessary columns from the OECD dataframe. functions are fun!
    droplist = ['Code', 'Women_avg_retirement_age', 'Men_avg_retirement_age']
    for column in droplist:
        dataframe = dataframe.drop(column, axis=1)
    return dataframe

print(column_dropper(oecd_df))
# plotting an experimental line graph of japan's retirement rates across the years, including both men and women. 
# the main goal is to create two graphs that compare japan/south korea's retirement rates to the oecd avg across both genders.

# japan_df_graph = japan_df.plot(kind = 'line', x = 'Year', 
#                                y = ['Women_avg_retirement_age', 'Men_avg_retirement_age'], 
#                                ylabel = ['Average retirement age (women)', 'Average retirement age (men)'], 
#                                legend = True)

# japan_df_testfig = japan_df_graph.get_figure()
# japan_df_testfig.savefig("japan_testfig.png") # added some code to test figure creation in vscode.
# test successful.

# next goal: find OECD average retirement age across both men and women.
# there are pandas functions to help with this, luckily. 



# making new graphs using the new dataframes.
'''
japan_df_graph = japan_df.plot(kind = 'line', x = 'Year', 
                               y = ['Women_avg_retirement_age', 'Men_avg_retirement_age', 'OECD_avg'], 
                               ylabel = 'Average retirement age: Japan vs OECD', 
                               legend = True)

japan_df_figure = japan_df_graph.get_figure()
japan_df_figure.savefig("japan_vs_oecd_fig.png")
'''