### Calendar Code

__GOALS__ 
  -  _`calendar_printer.py`:_ Create a program that creates a calendar using user input. It should be able to receive the number of days in a month and the starting day of the week, then print out a calendar according to those values. The first line should be the days of the week, starting from Monday. 
  - _`datetime_duration_calc.py`:_ Write a function that takes a date from a user and calculates the difference in days between that date and the current date. 
  - _`extended_duration_calc.py`:_ Write a function that takes a randomised set of dates (found in `random_dates.csv`) and returns the difference in days between those dates and the current date.

__NOTES__ 
  - `extended_duration_calc.py` is missing commented documentation. Simply put, the code imports the randomised dates and finds the current date. The `days_between_calc(provided_date)` function finds the difference between the provided date - which, in this case, would be the randomised date - and the current date. The `extended_duration_calc()` function converts each date in the CSV file into Numpy format, then prints how many days ago the randomised date was. It repeats this action for each date in the random list.
