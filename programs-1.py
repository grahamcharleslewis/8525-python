# Ask the user to input thier name, then display "Hello <name>!"
# Input / Output, string - concatenation, variable assignment
## name = input("Please enter your name: ")
## print("Hello " + name + "!")


# Ask the user to input some random text.
# Display the text and number of characters in the string.
# Input / Output, string - concatenation & formatting, variable assignment
## text = input("Please enter some text: ")
## print(text + " has " + str(len(text)) + " characters")


# Ask the user to input a quote, then ask the authors name.
# Display the name of the author and the quote in quote marks (").
# Input / Output, string - concatenation & formatting, variable assignment
## quote = input("Quote: ")
## author = input("Author: ")
## print(author + ' said "' + quote + '"')


# Ask the user for 2 integer numbers.
# Display the results of adding, subtracting, multiplying and dividing those two numbers.
# Input / Output, string - concatenation & formatting, variable assignment, string to number conversion
# and number to string conversion
## first_number = int(input("First number: "))
## second_number = int(input("Second number: "))
## print(str(first_number) + " + " + str(second_number) + " = " + str(first_number + second_number))
## print(str(first_number) + " - " + str(second_number) + " = " + str(first_number - second_number))
## print(str(first_number) + " * " + str(second_number) + " = " + str(first_number * second_number))
## print(str(first_number) + " / " + str(second_number) + " = " + str(first_number / second_number))


# Calculate the users retirement age.
# Ask the user for thier current age and the age at which they would like to retire.
# Display the number of years left they have to work, the current date and thier retirement date.
## current_age = int(input("Current age: "))
## retirement_age = int(input("Retirement age: "))
## current_year = int(input("What year is it: "))
## years_left = retirement_age - current_age
## print("You have " + str(years_left) + " years left to work")
## print("It is " + str(current_year) + ", you will retire in " + str(current_year + years_left))


# Calculate the area of a rectangular room.
# Ask the user for the length and width of the room feet.
# Display the input dimensions together with the area in square feet and meters.
# To caluclate square meters from square feet the formula is: square feet * 0.09290304
## FEET_TO_METER = 0.09290304
## room_length = int(input("Room length: "))
## room_width = int(input("Room width: "))
## area_in_square_feet = room_length * room_width
## area_in_square_meters = area_in_square_feet * FEET_TO_METER
## print(str(area_in_square_feet) + " square feet " + str(area_in_square_meters) + " square meters")


# Evenly divide a pizza.
# Ask the user how many people, how many pizzas, and how many slices per pizza you have in your party.
# NEEDS WRITING UP!!!
## people = int(input("How many people: "))
## pizzas = int(input("How many pizzas: "))
## slices_per_pizza = int(input("How many slices per pizza: "))
## total_slices = pizzas * slices_per_pizza
## whole_slices_per_person = total_slices // people
## remaining_pizza_slices = total_slices % people
## print(str(people) + " people with " + str(pizzas) + " and " + str(slices_per_pizza) + " slices per pizza")
## print("Each person gets " + str(whole_slices_per_person) + " slices")
## print("There are " + str(remaining_pizza_slices) + " slices left")


# Checkout.
# NEED WRITE UP
## checkout_subtotal = 0
## vat_percent = 5.5
## for i in range(3):
##     item_price = int(input("Item price [" + str(i + 1) + "]: "))
##     item_quantity = int(input("Item quantity [" + str(i + 1) + "]: "))
##     checkout_subtotal += item_price * item_quantity    
## vat = (vat_percent * checkout_subtotal) / 100
## print("Subtotal: £" + str(checkout_subtotal))
## print("VAT: £" + str(vat))
## print("Total: £" + str(checkout_subtotal + vat))


# Pounds to Euro currency conversion.
# NEEDS WRITE UP
pounds = int(input("Pounds: "))
exchange_rate = float(input("Exchange rate: "))
# euros = (pounds * exchange_rate) / 100
print(euros)
