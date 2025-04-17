# CONSOLIDATION TASK: PRACTICE LISTS - WAITER
# HELPER

starters = ({"name": "Soup", "price": 5.0},
            {"name": "Calamari", "price": 8.5},
            {"name": "Garlic Bread", "price": 6.0})
mains = ({"name": "Pizza", "price": 14.0},
         {"name": "Lasagne", "price": 16.0},
         {"name": "Burger", "price": 12.5},
         {"name": "Curry", "price": 14.0})
desserts = ({"name": "Brownie", "price": 10.0},
            {"name": "Sticky Toffee Pudding",
             "price": 9.5})

customer_ordered_list = []

print("Hello User! \nThese are the available "
      "starters:")
for option in starters:
    print("- " + option["name"])

chosen_starter = ""
successful = False
while not successful:
    chosen_starter = input("Which starter would "
                           "you like? ")
    for s in starters:
        if s["name"] == chosen_starter:
            chosen_starter = s
            successful = True
print("\nExcellent Choice!")
customer_ordered_list.append(chosen_starter)

print("\nThese are the available mains:")
for option in mains:
    print("- " + option["name"])

chosen_main = ""
successful = False
while not successful:
    chosen_main = input("Which main would "
                           "you like? ")
    for m in mains:
        if m["name"] == chosen_main:
            chosen_main = m
            successful = True
print("\nWonderful!")
customer_ordered_list.append(chosen_main)

print("\nThese are the available desserts:")
for option in desserts:
    print("- " + option["name"])

chosen_dessert = ""
successful = False
while not successful:
    chosen_dessert = input("Which dessert would "
                           "you like? ")
    for d in desserts:
        if d["name"] == chosen_dessert:
            chosen_dessert = d
            successful = True
print("\nSounds good!")
customer_ordered_list.append(chosen_dessert)

print(f"You ordered {chosen_starter['name']}, {chosen_main['name']}, and {chosen_dessert['name']}.")
price = chosen_starter["price"] + chosen_main["price"] + chosen_dessert["price"]
print(f"The total cost is £{price: .2f}")