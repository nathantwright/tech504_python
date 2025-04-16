"""
VARIABLES
"""
# PYTHON VARIABLE BASICS

num_var = 7567
dec_var = 3.14159
str_var = "Howdy!"

# == is a comparison operator that will return True
# if both sides of the operator are equal and False
# otherwise
print(str_var == "hi")

print(num_var, type(num_var))
print(dec_var, type(dec_var))
print(str_var, type(str_var))

# In a strongly typed language, data types are more
# strict. So the below code will work, but if the
# "str()" was removed then it would only work if
# Python was weakly typed.
print(str(num_var) + str_var)

# In a statically typed language, the type of a
# variable is fixed at creation. In a dynamically
# typed language (Python!) it can change.
new_var = 2.2
print(new_var, type(new_var))
new_var = "I'm a string now!"
print(new_var, type(new_var))

# Different objects have different ids (usually
# randomly generated at runtime. So changing the
# stored value also changes the id.
print(id(num_var))
num_var = 5555
print(id(num_var))

# Below, x and y represent the same thing, so
# they have the same id.
x = 10
y = x
print(id(x), id(y))

# Now x and y represent different things (y is
# still 10, but now x is 11) so their ids differ
x = 11
print(id(x), id(y))

user_name = input("Your name: ")
print(user_name)

user_name = input("Your name: ")
user_age = input("Your age: ")
user_dob = input("Your date of birth (dd-mm-yyyy): ")
print(user_name, user_age, user_dob)

print("Hi", user_name)