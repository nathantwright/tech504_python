"""DATA TYPES AND OPERATORS"""
# UNDERSTAND OPERATORS

# An operator represents a process, an operand is
# the data the process uses
x = 5
y = 1

print(x+y)
print(x-y)
print(x*2) # Multiply
print(x/2) # Divide
print(x//2) # Div (ignore remainder)
print(x%2) # Modulus (only remainder)

if 3 > 4:
    print("Three is greater than four")
if 3 < 4:
    print("Three is less than four")
if 3 == 4:
    print("Three is equal to four")
if 3 != 4:
    print("Three is not equal to four")
if 3 >= 4:
    print("Three is greater than or equal to four")
if 3 <= 4:
    print("Three is less than or equal to four")



# CREATE STRINGS AND USE QUOTES APPROPRIATELY

good_string_1 = "I said 'Wow!'"
good_string_2 = 'I said \'Wow!\''
good_string_3 = 'I said' + "'" + 'Wow!' + "'"
print(good_string_1)
print(good_string_2)
print(good_string_3)

# I think double quotes should be used unless they
# appear in the string



# SLICE STRINGS

# Slicing strings is getting parts of a string

Hw = "Hello world!"
print(Hw)

# Find out how many characters Hw has
print(len(Hw))

# Get the character in the first position in Hw
print(Hw[0])

# Get the last character
print(Hw[-1])

# Get the 2nd last character
print(Hw[-2])

# This prints all characters from index 2 (Letter
# 3) onwards
print(Hw[2:])

# This prints all characters from the third-to-last
# onwards (AKA last 3 chars)
print(Hw[-3:])

# This prints all characters up to index 5 (Indexes
# 0-4, first 5 chars)
print(Hw[:5])

# Starts from the second, stops at the fifth
# (doesn't include it)
print(Hw[1:4])



# FINISH THE GUESSING GAME WITH STRING SLICING

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code

original_word = "recommendation"
scrambled_word = "eoommandretnic"

# Create the hint slices...

# TO DO: On the next line, replace "?" with a
# string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint1_slice = original_word[4:6]

# TO DO: On the next line, replace "?" with a
# string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint2_slice = original_word[-3:]

# TO DO: On the next line, replace "?" with a
# string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint3_slice = original_word[7:10]

# TO DO: On the next line, replace "?" with a
# string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint4_slice = original_word[:2]

# Game instructions
print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

# Hints based on list slicing
print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
print("Hint 4: The first two letters are '" + hint4_slice + "'.")

# Game ends here
print("What's your guess?")