# compound interest calculator that takes initial savings amount, years of saving, number of compounding periods and the annual interest rate.
# for each year of savings it returns the total savings for that year. it also prints out how many years it would take for the savings amount 
# to double.

def comp_int_calculator():
    initial_saving = float(input("Enter your initial amount of savings: "))
    years = int(input("Enter the number of years you're saving for (whole numbers only): "))
    interest_rate = float(input("Enter the annual interest rate (decimal): "))
    doubled_saving = initial_saving * 2
    years_to_double = 0
    time = 0 # time acts as a counter between the starting year and the total years being saved for
    running_total = initial_saving # running_total is a variable amount, increasing with each calculation and increment of time
    for time in range(0, years): # for each year/compounding period up to the entered number of years
        print(f"Year {time}: £{running_total}")
        time += 1
        running_total = running_total * (1 + interest_rate)
        # running_total = initial_saving*(1 + interest_rate/comp_periods)**(comp_periods*time)
        if running_total >= doubled_saving: # NOTE: this method is ineffective. every year in which the running total is more than the inital amount of savings will be saved as the exact year where the amount hit double. this is wrong.
            years_to_double = time
    print(f"By year {years_to_double}, your savings amount will have doubled from £{initial_saving} to £{doubled_saving}.")
    

# def savings_double_calc():
#    initial_savings =  float(input("Enter your initial amount of savings: "))
#    interest_rate = float(input("Enter the annual interest rate (decimal): "))
#    doubled_savings = initial_savings * 2
#    years_to_double = 0# number of years it takes for the savings to double. for this, 'double' can be greater than or equal to 'doubled_savings'
    # incomplete
        
comp_int_calculator()
