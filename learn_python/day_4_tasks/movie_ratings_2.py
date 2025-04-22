# possible film ratings are
# "universal", "pg", "12", "12a", "15", "18"
ratings = ("universal", "pg", "12", "12a", "15", "18")

# use an if statement to check for "universal"
# rating
def print_description(film_rating):
    if film_rating == "universal":
        print("all age groups can watch this film")
    # check if film rating is "pg"
    elif film_rating == "pg":
        print("General viewing, but some scenes may be"
              " unsuitable for young children.")
    # check if film rating is "12" or "12a"
    elif film_rating == "12" or film_rating == "12a":
        print("Films classified 12A and video works "
              "classified 12 contain material that is "
              "not generally suitable for children "
              "aged under 12. No one younger than 12 "
              "may see a 12A film in a cinema unless "
              "accompanied by an adult.")
    # check if film rating is "15"
    elif film_rating == "15":
        print("No one younger than 15 may see a 15 "
              "film in a cinema.")
    # check if film rating is "18"
    elif film_rating == "18":
        print("No one younger than 18 may see an 18 "
              "film in a cinema.")
    else:
        print("This is not a correct rating, please "
              "use universal, pg, 12, 12a, 15, 18")

def get_rating():
    user_prompt = True
    rating =  ""
    while user_prompt:
        rating = input("What is the film rating? ")
        if rating.lower() not in ratings:
            print("Rating not found!\n")
        else:
            user_prompt = False
    return rating.lower()

loop = True
while loop:
    print_description(get_rating())
    print()
    invalid_y_n = True
    loop_again = "Y"
    while invalid_y_n:
        loop_again = input("Would you like to check another movie rating? Y/N: ")
        if loop_again.lower() == "y":
            print("Okay!\n")
            invalid_y_n = False
        elif loop_again.lower() == "n":
            print("Bye!")
            invalid_y_n = False
            loop = False
        else:
            print("Please input Y/N!")