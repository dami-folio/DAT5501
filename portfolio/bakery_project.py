# The goal of this project is to exercise my understanding of Python fundamentals and classes by making a bakery simulator. I've worked on this exact project before,
# but with limited success due to my lack of understanding and experience. As such, I am returning to try and complete a renewed version of the original code. 

# The bakery should have classes for menus, in which menu items are the class objects, and it should be possible to do the following:
#   - assign item types (e.g. baked good, beverage, confection, etc. )
#   - add menu items
#   - remove menu items
#   - assign prices to menu items within a price range (so that users can't sell drinks for £100)
#   - display menu items in a list (either all items at once or types of items at once)
#   - check menu item attributes (such as item name, price, type and whether or not it's currently discounted)

# Additionally, I'd like to try and create a basic customer algorithm so that selling items is actually possible. I would like for customers to have randomised budgets,
# and for them to be able to buy any number of bakery items as long as the total price falls within their budget. This is a secondary goal for this project, as the main
# goal is to practice object-oriented programming concepts and programming fundamentals.

class MenuItem:
    def __init__(self, ItemName, ItemType, ItemPrice, ItemDiscount):
        self.ItemName = ItemName
        self.ItemType = ItemType
        self.ItemPrice = ItemPrice
        self.ItemDiscount = ItemDiscount

class Menu: # menu class to contain items.
    def __init__(self, MenuItemName, MenuItemList, MenuItemCount, MenuNumber):
        self.MenuItemName = MenuItemName
        self.MenuItemList = MenuItemList
        self.MenuItemCount = MenuItemCount
        self.MenuNumber = MenuNumber


def menuManager(): # i'd like this function to handle all actions to do with modifying the menu. i'm not quite sure how possible this actually is.
    # i'd like to avoid using too much nesting. if i have to make separate menu management functions and nest them in here, that's fine, but
    # i'd rather limit nesting to solely this function (if that's possible)

    # requirements:
    #   - changing item names
    #   - removing items
    #   - changing item type
    #   - changing item price
    #   - setting alternate attributes such as discounts 
    #   - adding items
    menu_manage_prompt = input("What would you like to do?\n \n \t - [A]: New menu item\n \n \t - [B]: Cancel")
    if menu_manage_prompt.upper() == 'A':
        print('testing')
    if menu_manage_prompt.upper() == 'B':
        print('testing')
    else:
        print('invalid input')