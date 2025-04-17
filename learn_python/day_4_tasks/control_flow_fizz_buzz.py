for x in range(100):
    y = x+1
    if y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")
    elif y % 3 == 0:
        print("Fizz")
    elif y % 5 == 0:
        print("Buzz")
    else:
        print(y)