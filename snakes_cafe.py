print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

currOrder = ''
totalOrder = {}

while currOrder != 'quit':
    currOrder = input('> ')
    if currOrder != 'quit':
        if not (currOrder in totalOrder):
            totalOrder[currOrder] = 1
            print(f"\n** 1 order of {currOrder} has been added to your meal **\n")
        else:
            totalOrder[currOrder] = totalOrder[currOrder] + 1
            print(f"\n** {totalOrder[currOrder]} orders of {currOrder} have been added to your meal **\n")
    else:
        cost = 0;
        for order in totalOrder:
            print(f"** {totalOrder[order]} orders of {order}**")
            cost += totalOrder[order] * 5
        print(f"\n ** Your total will be ${cost}.00 plus tax and tip **\n")
