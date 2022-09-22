"""
CP1404 | Practical 01: Shop Calculator | Tahlia Clennar
Program to compute and display total price of items
"""
# initializing prices
price_of_item = 0
total_price_of_items = 0

# getting user input
number_of_items = int(input("Number of items: "))

# checking for errors
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# calculating total cost of items
for i in range(number_of_items):
    price_of_item = float(input("price_of_item : "))
    total_price_of_items = price_of_item + total_price_of_items

# conditional logic to receive a 10% discount if total price is greater than $100
if total_price_of_items > 100:
    total_price_of_items = 0.9 * total_price_of_items

# printing the total cost and number of items
print(" Total price for {} items is {:.2f}". format(number_of_items, total_price_of_items))


