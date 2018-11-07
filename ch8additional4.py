#Arik Parenteau
#Gabe Sorenson

menu = {'Taco': 6.99, 'Cheeseburger': 7.50, 'Lasagna': 10.99, 'Chili cheese fries': 8.25,
        'Poutine': 5.99, 'Soup and salad': 7.99, 'Steak': 12.99 }
	
def displayMenu():	
    print('MENU')
    for key, value in menu.items():
        print('%s: $%.2f' % (key, value))


def chooseDealItems():
    print("\nToday's deal: choose any 2 items for %10 off\n(cannot choose 2 of the same).")
    print('Enter -1 for the second menu item if only 1 menu item is desired')
    food1 = input('\nEnter first menu item:\n')
    while food1 not in menu:
        print('Item not on menu. Try again.')
        food1 = input('Enter first menu item:\n')
    price1 = menu[food1]
    menu.pop(food1)
    print()
    displayMenu()
    food2 = input('\nEnter second menu item:\n')
    while food2 not in menu and food2 != '-1':
        print('Item not on menu. Try again.')
        food2 = input('Enter second menu item or -1:\n')

    if food2 != '-1':
        price2 = menu[food2]
    else:
        price2 = 0
    return food1, price1, food2, price2


displayMenu()
item1, money1, item2, money2 = chooseDealItems()
print('\nRECEIPT')
print('Item: %s  Cost: $%.2f' %(item1, money1))
if item2 == '-1':
    print('Total Cost: $%.2f' % money1)
else:
    print('Item: %s  Cost: $%.2f' % (item2, money2))
    total = 0.8 * (money1 + money2)
    print('Total Cost: $%.2f' % total)
    saved = (money1 + money2) - total
    print('Money Saved: $%.2f' % saved)
