# shopping_cart.py

import datetime
products = [
    {"id": 1, "name": "Chocolate Sandwich Cookies",
        "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id": 2, "name": "All-Seasons Salt", "department": "pantry",
        "aisle": "spices seasonings", "price": 4.99},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea",
        "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
        "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry",
        "aisle": "marinades meat preparation", "price": 7.99},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care",
        "aisle": "cold flu allergy", "price": 21.99},
    {"id": 7, "name": "Pure Coconut Water With Orange",
        "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash",
        "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt",
        "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage",
        "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages",
        "aisle": "refrigerated", "price": 1.99},
    {"id": 12, "name": "Chocolate Fudge Layer Cake",
        "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care",
        "aisle": "cold flu allergy", "price": 16.00},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner",
        "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id": 15, "name": "Overnight Diapers Size 6",
        "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup",
        "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood",
        "aisle": "poultry counter", "price": 9.99},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza",
        "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend",
        "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink",
        "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# def to_usd(my_price):
#     """
#     Converts a numeric value to usd-formatted string, for printing and display purposes.

#     Param: my_price (int or float) like 4000.444444

#     Example: to_usd(4000.444444)

#     Returns: $4,000.44
#     """
#     return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

# print(products)


total_price = 0
selected_product = []
valid_id = []

for p in products:
    valid_id.append(str(p["id"]))


while True:
    selected_id = input("Please enter your product: ")
    if selected_id == "DONE" or selected_id == "done" or selected_id == "Done":  # exiting when DONE
        break
    elif selected_id not in valid_id:
        print("You selected an invalid id, please re-enter")
    elif selected_id in valid_id:
        selected_product.append(selected_id)  # Collecting the items in a list


now = datetime.datetime.now()


print("************************************************************************************************************")


print("                                            CORONA-FREE DELI                                                ")
print("                                  888 Hope Avenue, Manhattan, NY 88888                                      ")
print("                                       www.corona_free_deli.com                                             ")

print("                                          Visit Date and Time:                                            ")
print("                                          " +
      now.strftime("%Y-%m-%d %H:%M:%S"))

print("************************************************************************************************************")
print("************************************************************************************************************")


for selected_id in selected_product:
    matching_ids = [p for p in products if str(p["id"]) == str(
        selected_id)]  # look up for selected product
    matching_id = matching_ids[0]  # first one on the list
    total_price = total_price + matching_id["price"]
    print(" ------" + "Yours Now :) --> " +
          matching_id["name"] + " " + "(" + "$" + str(matching_id["price"]) + ")")

print("************************************************************************************************************")


def to_usd(total_price):
    return f"${total_price:,.2f}"  # > $12,000.71


print(" ------SUBTOTAL: " + "        " + to_usd(total_price))


def tax(total_price):
    return total_price*0.0875


x = tax(total_price)


def t_to_usdd(x):
    return f"${x:,.2f}"


print(" ------TAX: " + "             " + t_to_usdd(x))


def total_w_tax(total_price):
    return (total_price*1.0875)-1


t = total_w_tax(total_price)


def to_usdd(t):
    return f"${t:,.2f}"


smile_disc = 1


def discount(smile_disc):
    return f"${smile_disc:,.2f}"  # > $12,000.71


print(" ------SMILE DISCOUNT:" + "   " + discount(smile_disc))


print(" ------TOTAL:" + "            " + to_usdd(t))


print("************************************************************************************************************")
print("************************************************************************************************************")


print("****************************THANKS FOR VISITING FRIEND, YOU MADE OUR DAY!***********************************'")

