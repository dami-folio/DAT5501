# code goals: write a function that takes date input from the user and calculates how many days it is until 
# the current date.

import numpy as np

def receive_date():
    given_date = np.datetime64(input("Enter a date in the YYYY-MM-DD format: ")) # takes a date from the user and converts it into the np.datetime64 format
    return given_date

# given_date = receive_date() # takes a date given by the user.
current_date = np.datetime64('Today', 'D') # retrieves the current date.
given_date = np.datetime64("1999-01-01")

def datetime_diff_calc(provided_date):
    days_until_today = current_date - provided_date
    return days_until_today

days_until_today = datetime_diff_calc(given_date)

# print(f"There are {days_until_today} until today from {given_date}.")
