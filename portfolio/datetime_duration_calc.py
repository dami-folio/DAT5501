# code goals: write a function that takes date input from the user and calculates how many days it is until 
# the current date.

import numpy as np
import datetime

def receive_date():
    given_date = np.datetime64(input("Enter a date in the YYYY-MM-DD format: "))
    return given_date

given_date = receive_date()
current_date = np.datetime64('Today', 'D')


def datetime_diff_calc():
    days_until_today = current_date - given_date
    return days_until_today

days_until_today = datetime_diff_calc()

print(f"There are {days_until_today} until today from {given_date}.")

