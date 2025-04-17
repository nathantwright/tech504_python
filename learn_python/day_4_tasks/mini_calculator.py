def add():
    print("\nYou want to add: a + b, "
          "what should 'a' be?")
    a = ask()
    print(f"\nYou want to add: {a} + b, "
          "what should 'b' be?")
    b = ask()
    return a + b

def sub():
    print("\nYou want to subtract: a - b, "
          "what should 'a' be?")
    a = ask()
    print(f"\nYou want to subtract: {a} - b, "
          "what should 'b' be?")
    b = ask()
    return a - b

def mul():
    print("\nYou want to multiply: a x b, "
          "what should 'a' be?")
    a = ask()
    print(f"\nYou want to multiply: {a} x b, "
          "what should 'b' be?")
    b = ask()
    return a * b

def div():
    print("\nYou want to divide: a / b, "
          "what should 'a' be?")
    a = ask()
    print(f"\nYou want to divide: {a} / b, "
          "what should 'b' be?")
    b = ask()
    return a // b

def in_val():
    return int(input("\nWhat value? "))

def ask():
    choice = -1
    while choice > 4 or choice < 1:
        choice = int(input("add (1), "
                           "\nsubtract (2), "
                           "\nmultiply (3), "
                           "\ndivide (4), "
                           "\ninsert value (5)? "))
        if choice == 1:
            return add()
        elif choice == 2:
            return sub()
        elif choice == 3:
            return mul()
        elif choice == 4:
            return div()
        elif choice == 5:
            return in_val()

print("Answer is", ask())