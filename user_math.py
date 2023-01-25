"""
Always start with a docstring that describes what the module does.
Include your name and the date.



Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

def lesson_count_per_week(mon, tue, wed, thur, fri):
    """
    Returns the sum of horse riding lessons given per week
    
    """
    try:
        lesson_count = math.fsum([mon + tue + wed + thur +fri])
        return lesson_count
    
    except Exception as ex:
        print(f"Error: {ex}")
        return None
        

#-------------------------------------------------------------

def daily_average_count(mon, tue, wed, thur, fri):
    """
    Returns the average number of horse riding lessons given in a week

    """
    try:
        week_total = mon + tue + wed + thur + fri
        daily_average_count = math.floor(week_total / 5)
        return daily_average_count
    
    except Exception as ex:
        print(f"Error: {ex}")
        return None

#--------------------------------------------------------------

def earnings_per_week(mon, tue, wed, thur, fri):
    """
    Returns the horse riding lesson earnings per week
    
    """
    try:
        week_total = mon + tue + wed + thur + fri 
        daily_average_count = math.ceil(week_total / 5)
        earnings = week_total * daily_average_count
        return earnings
    
    except Exception as ex:
        print(f"Error: {ex}")
        return None



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Module 2 Project")
    print("Chelsea Brammer, 1/21/23")
    print("Horseback Riding Trainer Analysis")

    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1,)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()

print("The are of lot (6,2) is:", get_area_of_lot(6,2))
print()

print(f"Number of horseback riding lessons given this week = {lesson_count_per_week(10, 5, 7, 9, 6)} ")
print()
print(f"The average number of horseback riding lessons given in one day = {daily_average_count(10, 5, 7, 9, 6)} ")
print()
print(f"The total earnings per week = {earnings_per_week(10, 5, 7, 9, 6)} ")
