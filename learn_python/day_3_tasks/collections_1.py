# WORKING WITH A LIST
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list[1] = "rice"
print(shopping_list[1])
shopping_list.append("carrots")
print(len(shopping_list))
new_list = ["toffee", "coffee"]
shopping_list.extend(new_list)
print(shopping_list)
shopping_list.remove("bananas")
print(shopping_list)
shopping_list.pop()
print(shopping_list)



# MIX ALL THE DATA ABOUT A USER INTO A LIST
user_name = input("Your name: ")
user_age = input("Your age: ")
user_dob = input("Your date of birth (dd-mm-yyyy): ")
height = input("Enter your height (cm): ")
user_details_list = [user_name, int(user_age), user_dob, float(height)]
print(user_details_list)
