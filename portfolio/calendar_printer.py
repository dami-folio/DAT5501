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
    calendar_complete = False
    counter = 0
    for week in range(1, weeks):
        if week == 1: # if it's the first week in the calendar....
            for not_starting_day in range(1, starting_day):
                counter += 1
                calendar_str += "--  " #... then for each day before the starting day of the month, print filler characters.
        else: # if it's not the first week...
            while calendar_complete == False:
                for day in range(1, days_in_month + 1): #... then for every day in the month...
                    if day == days_in_month + 1: # check if this is the final day of the month.
                        calendar_complete = True # if it is, then the calendar is complete and the loop ends.
                    else:
                        if counter != 7: # if the counter hasn't reached 7..
                            calendar_str += f"{day} " # ..add a day onto the calendar string and increment the counter by 1.
                            counter += 1 
                        else: # otherwise, start a new line and reset the counter.
                            calendar_str += "\n"
                            counter = 0

    print(calendar_str)

calendar_printer()