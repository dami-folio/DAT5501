# GOAL: create a program that prints out a calendar based on user input.
# it should be able to take the number of days in a month and the day that each week starts on.
# the first line should be the days of the week: Mon, Tue, Wed, Thur, Fri, Sat, Sun.
# NOTE: if the week starts on wednesday, then the numbered days should start from wednesday. the spaces for monday and tuesday should be blank.

def calendar_printer():
    days_in_month = int(input("How many days are in a month? Please enter an integer: "))
    starting_day = input("Select which day each week starts on from the list below using the corresponding letter ONLY: \n [A] - Monday\n [B] - Tuesday\n [C] - Wednesday\n [D] - Thursday\n [E] - Friday\n [F] - Saturday\n [G] - Sunday\n\n")

