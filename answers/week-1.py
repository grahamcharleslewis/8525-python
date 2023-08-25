def get_input(prompt):
    return int(input(prompt + ": "))

def print_output(years_left, current_year, retirement_year):
    print("You have " + str(years_left) + " years left to work")
    print("It is " + str(current_year) + ", you will retire in " + str(retirement_year))
    
def process_data(current_age, retirement_age, current_year):
    years_left = retirement_age - current_age
    retirement_year = current_year + years_left
    return years_left, retirement_year
    
current_age = get_input("Current age")
retirement_age = get_input("Retirement age")
current_year = get_input("What year is it")

years_left, retirement_year = process_data(current_age, retirement_age, current_year)

print_output(years_left, current_year, retirement_year)
