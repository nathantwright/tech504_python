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

customer_count = int(input("Hello User! \nHow many"
                           " are in your party? "))
print("These are the available starters:")
for option in starters:
    print("- " + option["name"])

for c in range(customer_count):
    chosen_starter = ""
    successful = False
    while not successful:
        chosen_starter = input(f"Customer #{c+1}, "
                               f"which starter "
                               f"would you like? ")
        for s in starters:
            if s["name"] == chosen_starter:
                chosen_starter = s
                successful = True
    print("\nExcellent Choice!")
    customer_ordered_list.append(chosen_starter)

print("\nThese are the available mains:")
for option in mains:
    print("- " + option["name"])

for c in range(customer_count):
    chosen_main = ""
    successful = False
    while not successful:
        chosen_main = input(f"Customer {c+1}, "
                            f"which main would "
                            f"you like? ")
        for m in mains:
            if m["name"] == chosen_main:
                chosen_main = m
                successful = True
    print("\nWonderful!")
    customer_ordered_list.append(chosen_main)

print("\nThese are the available desserts:")
for option in desserts:
    print("- " + option["name"])

for c in range(customer_count):
    chosen_dessert = ""
    successful = False
    while not successful:
        chosen_dessert = input(f"Customer {c+1}, "
                               f"which dessert "
                               f"would you like? ")
        for d in desserts:
            if d["name"] == chosen_dessert:
                chosen_dessert = d
                successful = True
    print("\nSounds good!")
    customer_ordered_list.append(chosen_dessert)

print(f"You ordered {customer_ordered_list}.")
price = 0.0
for o in customer_ordered_list:
    price += o["price"]
print(f"The total cost is £{price: .2f}")