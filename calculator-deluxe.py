import time

# Calculator - Deluxe Edition
# Name and version info
version_info = "MyCalculator - Deluxe Edition v0.3"


# Function for getting menu choice
def get_menu_choice():
    # Variable used to align the menu to a common width
    menu_width = 30

    # List of available menu options
    valid_menu_choice = ['+', '-', '*', '/', 'e']

    # Loop until valid choice is made. If illegal input, ask the user again
    while True:
        print('\n')
        print('*' * menu_width)
        print("Welcome to " + version_info)
        print('*' * menu_width)
        print("Choose type of calculation or exit")
        print('*' * menu_width)
        print("* Addition:       +")
        print("* Subtraction:    -")
        print("* Multiplication: *")
        print("* Division:       /")
        print("* Exit:           e")
        print('*' * menu_width)
        choice = input("Please choose your option: ")

        # If the user input is valid, exit the loop by returning from the function with the user choice
        if choice in valid_menu_choice:
            return choice

        # If the user did not input a valid choice, inform about valid options, and ask again
        else:
            print(f"\n\t** Illegal menu option, please use one of {valid_menu_choice}")
            time.sleep(1)


# Function for reading in a number, and ensuring that the input is valid
def read_input_number():
    while True:
        input_number = input("Please input number: ")
        if input_number.isdigit():
            return int(input_number)
        else:
            print(f"\n\t** {input_number} is not valid, try again")
            time.sleep(1)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(a, b, operator):
    if operator == '+':
        return addition(a, b)
    elif operator == '-':
        return subtraction(a, b)
    elif operator == '*':
        return multiplication(a, b)
    elif operator == '/':
        return division(a, b)


# Variable for storing the user menu choice
menu_choice = get_menu_choice()

# Loop the whole program until the user choice is 'e' (exit)
while menu_choice != 'e':
    # Get the two numbers from the user
    number_a = read_input_number()
    number_b = read_input_number()

    # Calculate based on chosen operator and input numbers
    result = calculate(number_a, number_b, menu_choice)

    # Print results of calculation
    print(f"\n** Calculation {number_a} {menu_choice} {number_b} = {result}\n")
    time.sleep(1)

    menu_choice = get_menu_choice()


# The loop is finished and we exit the program
print(f"\nThank you for using {version_info}")
print("Goodbye")
