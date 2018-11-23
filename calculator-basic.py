# Calculator - Basic Edition

# Name and version info
version_info = "MyCalculator - Basic Edition v1.0"


# Function to add two numbers, and returning the result
def add_numbers(a, b):
    return a + b


# Print welcome text
print('\n')
print('*' * 50)
print("Welcome to " + version_info)
print("This calculator let you add two numbers")
print('*' * 50 + '\n')

# Variable to keep track of the user choice to continue or exit
user_exit = False

# Repeat until the user choose to exit
while not user_exit:

    # Get user to input numbers to be calculated
    number_a = int(input("Please input the first number: "))
    number_b = int(input("Please input the second number: "))

    # Calculate result
    result = add_numbers(number_a, number_b)

    # Print answer
    print(f"The two numbers added are: {result}")

    # Ask if user want to do more calculations
    answer = input("\nDo you want to calculate more? (y/n) ")
    # Ensure input is in lower case so both y/n and Y/N are valid inputs
    answer = answer.lower()
    if answer != 'y':
        user_exit = True

# Print goodbye message
print("\nThank you for using " + version_info)
print("Goodbye...")
