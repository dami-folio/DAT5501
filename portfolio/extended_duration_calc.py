import numpy as np

random_dates = np.loadtxt("random_dates.csv", dtype = "str")
current_date = np.datetime64('Today', 'D')

def days_between_calc(provided_date):
    return current_date - provided_date

def extended_duration_calc():
    for date in random_dates:
        date = np.datetime64(date)
        print(f"There are {days_between_calc(date)} until today from {date}.")

extended_duration_calc()