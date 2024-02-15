# Author: Jordan Chun Yin Cheung
# Program: Conversion calculator
# Purpose: Convert decimal numbers to binary or binary to decimal

from os import name, system

def clear_screen():
    # clear the screen to see better
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    binary_result = ""                   # Initialize an empty string to store the binary representation
    if decimal_num == 0:                 # Check if dec num is 0

        return "0"                       # If the input is 0, return "0" as the binary representation
    while decimal_num > 0:               # Use a while loop to calculate the binary representation

        remainder = decimal_num % 2       # Calculate the remainder when dividing the decimal number by 2
        binary_result = str(remainder) + binary_result       # Convert the remainder to a string and add it to the beginning of the binary result
        decimal_num = decimal_num // 2    # Update the decimal number by performing integer division by 2
    return binary_result                  # Return the final binary representation

# Function to convert binary to decimal
def binary_to_decimal(number):
    result = 0                              # Initialize the decimal result
    if len(number) > 0:                     # Check if the binary number has at least one digit
        power = len(str(number)) - 1        # Determine the greatest power of 2 by subtracting 1 from the length of the binary number
        for num in str(number):             # Iterate through each digit in the binary number
            result += int(num) * 2 ** power # Calculate the decimal representation using the current digit and power of 2
            power -= 1                      # Decrease the power by 1 for the next iteration
    return result                           # Return the final decimal result

# Verify if it is a decimal
def is_decimal(numbers):
    dec_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number not in dec_list:
            print("{} is not a decimal number".format(number))
            return False
        return True

# Verify if it is a binary
def is_binary(numbers):
    bin_list = ["0", "1"]
    for number in numbers:
        if number not in bin_list:      # Input is not in bin_list print:
            print( "{} is not a binary number".format(number))
            return False
    return True

# Get the conversion menu
def get_menu():
    print("\n-----Cheung's Conversion Calculator-----")
    menu_dict = {                               # Menu dictionary
        '1': 'Binary to decimal',
        '2': 'Decimal to binary',
        '3': 'Binary to hexadecimal',
        '4': 'Decimalto hexadecimal',
        '5': 'Octal to decimal',
        '6': 'Decimal to octal',
        '7': 'Hexadecimal to binary',
        '8': 'Hexadecimal to decimal',
        'X': 'Exit/quit calculator'
    }
    return menu_dict

# Display the menu
def display_menu(menu_dict):
    for items, values in menu_dict.items():
        print(items + ". " + values.replace('_', ' ').capitalize())

    # Get user input
    menu_selection = input("Which conversion calculator do you want to use: ").upper()
    print("\nYou have selected: {}".format(menu_dict[menu_selection]))  # (menu_dict[menu_selection]) this makes the number input into the wording that is listed to the number
    return menu_selection

# Verify user selection
def is_valid_selection(menu_selection):
    menu_dict = ["1", "2", "X"]
    if menu_selection not in menu_dict:
        print("{} is not on the selection menu".format(menu_selection))
        return False
    return True

# Main function
def main():
    clear_screen()
    print("Hello User,")
    print("Welcome to Cheung's Conversion Calculator")
    print("This is where you put a binary number in, and it will give you the decimal or vice versa.")
    print("Binary numbers: 0, 1")
    print("Decimal numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
    print("\nHere's a list of options that is build in this program:")

    menu_selection = ''
    while menu_selection != 'X':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)

# When user inputs a "X" it will print these:
        if menu_selection == "X":
            print("Thank you for using Cheung's conversion-calculator!!!")
            print("Exiting the program...")
            print("Goodbye!!!")
            break

        if menu_selection in ['3', '4', '5', '6', '7', '8']:        # If the user entered "3-8" then will do the print statements.
            print("The selected function has not been coded yet.")
            print("Sorry for the inconvenience. :(")
            continue        # Will return to the menu_selection

# Printed after selecting from the list
        user_input = input("Enter the {} number: ".format("binary" if menu_selection == '1' else "decimal"))
        if not user_input or (menu_selection == '1' and not is_binary(user_input)) or (menu_selection == '2' and not is_decimal(user_input)):
            print("Invalid input. Please enter a valid {} number.".format("binary" if menu_selection == '1' else "decimal"))    # This formats the {} in binary if input is 1 or else it will be decimal)
            continue


        if menu_selection == '1':       # If you entered "1", it will do the formula for bin to dec
            result = binary_to_decimal(user_input)
            print("Binary {} --> Decimal {}".format(user_input, result))

        else:     # Otherwise it will do this if you entered "2"
            result = decimal_to_binary(int(user_input))
            print("Decimal {} --> Binary {}".format(user_input, result))

# Executes the def main()
if __name__ == "__main__":
    main()
