# User story 1
# As a user, I want to be able to guess a number
# and know if I got it correct or not, so that I
# can know if I won or not.
# User story 2
# As a user, I want to be able to guess a number
# and know if I need to go higher or lower.
# User story 3
# As a user, I don't want my guesses wasted if I
# enter something accidentally as my guess which
# are not digits.
# User story 4
# As a user, after each guess, I would like to know
# how many guesses I have left.
# User story 5
# As a user, I would like the magic to be randomly
# generated each time I play so it is more fun.
# User story 6
# As a user, I would like to know the magic number
# at the end of the game if I still haven't guessed
# correctly and I've used up all my tries.


import random

# Define/assign number to a variable called
# magic_number
magic_number = random.randint(1,50)

won = False

# Function to get input without error
def get_input():
    user_prompt = True
    #num = 0

    while user_prompt:
        num = input("What do you think the magic "
                      "number is? ")
        if not num.isdigit():
            print("Not recognised as digits!")
        else:
            user_prompt = False

    return num



# Allow the user 5 guesses
for c in range(5):

    # Ask user for input
    guess = int(get_input())

    # Check if this input matches magic_number
    if guess == magic_number:
        # Let the user know if the response was correct
        # or not
        print("Yes!")
        won = True
        break
    else:
        if guess > magic_number:
            print("Too high!")
        else:
            print("Too low!")
        print(f"Guesses remaining: {4-c}")

if not won:
    print(f"\nThe number was: {magic_number}")