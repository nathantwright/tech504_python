# TEST YOU CAN SLICE LISTS
mixture = [1, 2, 3,"one", "two", "three"]
print(mixture)

print(mixture[1:3])
print(mixture[0::2])
print(mixture[-1::-1][0:2])



# LEARN TUPLES - FINISH ISLAND GAME

"""
Tuples are essentially lists which can't be 
  modified, this is whats known as "immutable"
Strings, ints, floats, Booleans, etc... are all 
  immutable, meaning the variables of those types
  can be reassigned but not modified.
Tuples are useful when the values shouldn't be able
  to change. So, the months of the year could be 
  stored in a tuple because they don't change.
"""
essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
"""
The above code creates and prints a tuple, and then
  prints the number of occurrences of the string 
  "bread" in that tuple.
"""

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You "
      "can take only THREE items.")
essential_item1 = input("What is an essential item"
                        " you would take? ")
essential_item2 = input("What is an essential item"
                        " you would take? ")
essential_item3 = input("What is an essential item"
                        " you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1,
                    essential_item2,
                    essential_item3)
# print the tuple
print("Here are your items as a tuple:",
      essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more "
                        "essential item you would "
                        "take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to
# save the 4th item to the tuple
essentials_tuple += (essential_item4,)
print("Here are your items as a tuple (with the "
      "4th item added):", essentials_tuple)