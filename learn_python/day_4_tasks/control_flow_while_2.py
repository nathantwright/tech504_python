user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if not age.isdigit():
        print("Not recognised as digits!")
    elif int(age) > 117:
        print("Age too high!")
    else:
        user_prompt = False

print(f"Your age is {age}")