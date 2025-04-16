import time

age_int = int(input("What is your age? "))
name_str = input("What is your name? ")

current_datetime = time.gmtime()
nice_datetime = time.strftime("%d-%m-%Y", current_datetime)

hours_lived = (age_int+0.5)*(365.25*24)

print(f"Wow {name_str}, you are {age_int} years"
      +" old so you were born in "
      +f"{int(nice_datetime[-4:])-age_int}")
print(f"You have lived about {hours_lived} hours!")