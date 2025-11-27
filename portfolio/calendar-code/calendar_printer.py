# GOAL: create a program that prints out a calendar based on user input.
# it should be able to take the number of days in a month and the day that each week starts on.
# the first line should be the days of the week: Mon, Tue, Wed, Thur, Fri, Sat, Sun.
# NOTE: if the week starts on wednesday, then the numbered days should start from wednesday. the spaces for monday and tuesday should be blank.

def calendar_printer():
    days_in_month = int(input("How many days are in the month? Please enter an integer: "))
    weeks = days_in_month // 7 # a counter for the calendar to try and measure up to. once week_num matches this number, end the loop
    leftover_days = days_in_month % 7 # days that wouldn't make up one whole week. so, if there are 15 days in a month, there'd be 1 leftover day.
    if leftover_days > 0: # in the case that there are 'leftover days', or days that don't fill up one whole weeks, add an extra week onto the counter.
        weeks = weeks + 1
    starting_day = int(input("Select the starting day for the week. Monday - 1, Tuesday - 2, Wednesday - 3...: "))
    print("M.  T.  W.  T.  F.  S.  S.") # this doesn't need to shift to match the starting day - it should be static. 
    calendar_str = ""
    for week in range(1, weeks):
        if week == 1:
            for not_starting_day in range(1, starting_day):
                calendar_str += "--  "
        else:
            for day in range(1, days_in_month + 1):
                if day % 7 != 0:
                    calendar_str += f"{day} "
                else:
                    calendar_str += "\n"

    print(calendar_str)

calendar_printer()