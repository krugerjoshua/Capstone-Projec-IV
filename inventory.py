# ----- Import Section ----- #
from tabulate import tabulate
# ----- Class section ------ #

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        print(self.cost)

    def get_quantity(self):
        print(self.quantity)

    def __str__(self):
        return 

# ---- Function Section ---- #

shoes = []

def read_shoe_data():
    try:
        with open('inventory.txt', 'r') as f:
            next(f) # Skip the first line.
            for line in f:
                country, code, product, cost, quantity = line.strip().split(",")
                cost = int(cost)
                quantity = int(quantity)
                shoes.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("The file 'inventory.txt' has not been found.")

def capture_shoes():
    country = input("Enter Country: ")
    code = input("Enter the Code: ")
    product = input("Enter the Product: ")
    cost = int(input("Enter the Price: R"))
    quantity = int(input("Enter the Quantity: "))
    shoes.append(shoes(country, code, product, cost, quantity))
    with open('inventory.txt', 'a') as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")
        f.close()

def view_all():
    f = open('inventory.txt', 'r')
    list_dict = [
    ]
    for line in f:
        stripped_line = line.strip("\n")
        line_list = stripped_line.split(",")
        list_dict.append(line_list)
    print(tabulate(list_dict, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity'], tablefmt = 'rst'))

def re_stock(): # Used the lambda function to get the lowest value in quantity. Link below to stack overflow
    read_shoe_data()
    min_quantity = min(shoes, key=lambda x: x.quantity).quantity # https://stackoverflow.com/questions/54624235/how-to-search-list-of-objects-for-index-of-minimum
    shoes_to_restock = [shoe for shoe in shoes if shoe.quantity == min_quantity]
    for shoe in shoes_to_restock:
        print(f"Shoe code: {shoe.code}, Quantity: {shoe.quantity}")
        add_quantity = input("Do you want to add the quantity of these shoes? (y/n)")
        if add_quantity.lower() == "y":
            quantity = int(input("Enter the quantity to add: "))
            shoe.quantity += quantity
            with open("inventory.txt", "w") as f:
                for shoe in shoes:
                    f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        elif add_quantity.lower() == "n":
            break
        else:
            print("Wrong selection please retry")
            continue

def search_shoe():
    user_search = input("Enter Product Code: ")
    f = open('inventory.txt', 'r')
    for line in f:
        strip_line = line.strip().split(',')
        if user_search == strip_line[1]:
            print(f"Country: {strip_line[0]}")
            print(f"Code: {strip_line[1]}")
            print(f"Product: {strip_line[2]}")
            print(f"Cost: R{strip_line[3]}.00")
            print(f"Quantity: {strip_line[4]}")

def value_per_item(): # value = cost * quantity
    f = open('inventory.txt', 'r')
    object_dict = [
        []
    ]
    for line in f:
        strip = line.strip().split(',')    
        value = int(strip[3]) * int(strip[4])
        strip.append(value)
        object_dict.append(strip)

    print(tabulate(object_dict, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Total Value (R)'], tablefmt = 'rst'))

def highest_qty():
    read_shoe_data()
    max_quantity = max(shoes, key=lambda x: x.quantity).quantity
    shoes_to_restock = [shoe for shoe in shoes if shoe.quantity == max_quantity]
    for shoe in shoes_to_restock:
        print(f"{shoe.product}({shoe.code}) with a quantity of {shoe.quantity} should be put on sale.")

# ------ Main Section ------ #

while True:
    print("------------------------------------------------------------")
    print("Welcome to Inventory Control")
    print("What would you like to do?(Only enter the first 2 letters)")
    print("""------------------------------------------------------------
cs = Add shoes to inventory
va = View all stock
ls = View product with lowest stock levels
ss = Search for a product
vi = Show the total value for all stock
hq = Show the product with the highest quantity
ex = Exit the program
------------------------------------------------------------""")
    user_choice = input(": ")
    print(" ")
    user_choice.lower()

    if user_choice == "cs":
        capture_shoes()
        continue

    elif user_choice == "va":
        view_all()
        continue

    elif user_choice == "ls":
        re_stock()
        continue

    elif user_choice == "ss":
        search_shoe()
        continue

    elif user_choice == "vi":
        value_per_item()
        continue

    elif user_choice == "hq":
        highest_qty()
        continue

    elif user_choice == "ex":
        print("GoodBye!")
        break

    else:
        print("Invalid selection")
        continue