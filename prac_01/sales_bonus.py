"""
CP1404 | Practical 1:Sales bonus | Tahlia Clennar
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# getting user input
sales = float(input("Enter sales: $"))

while sales >= 0:
    # conditional logic for receiving a 10% bonus
    if sales < 1000:
        bonus = 0.1 * sales
        # displaying the user's bonus
        print("The user bonus is: {:.2f}".format(bonus))

    else:
        # calculating 15 % bonus
        bonus = 0.15 * sales
        # displaying the user's bonus
        print("The user bonus is: {:.2f}".format(bonus))
    # getting the user input again
    sales = float(input("Enter sales: $"))
