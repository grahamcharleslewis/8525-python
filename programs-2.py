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


# # Pounds to Euro currency conversion.
# # NEEDS WRITE UP
# pounds = int(input("Pounds: "))
# exchange_rate = float(input("Exchange rate: "))
# # euros = (pounds * exchange_rate) / 100
# print(euros)
