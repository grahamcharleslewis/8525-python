# ================================================================================
# HOMEWORK
# ================================================================================

# Calculate the users retirement age.
# Ask the user for thier current age and the age at which they would like to retire.
# Display the number of years left they have to work, the current date and
# thier retirement date.

# Example...
# Current age: 50
# Retirement age: 65
# What year is it: 2000
# You have 15 years left to work
# It is 2000, you will retire in 2015

# Answer...
current_age = int(input("Current age: "))
retirement_age = int(input("Retirement age: "))
current_year = int(input("What year is it: "))

years_left = retirement_age - current_age
retirement_year = current_year + years_left

print("You have " + str(years_left) + " years left to work")
print("It is " + str(current_year) + ", you will retire in " + str(retirement_year))
