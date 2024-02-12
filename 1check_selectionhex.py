def check_selection(numbers):
    #Verifies if the input is a hexadecimal number.
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() not in hex_list:
            print("{} is not a hexadecimal".format(number))
            return (False)  # Return False immediately if a non-hex character is found
    return (True)  # All characters are hex, so return True

def main():
    #Prompts for a hexadecimal number until a valid one is entered.
    good_selection = False
    while not good_selection:  # Loop continues as long as good_selection is not True
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selection(selection)
    print("Good job", selection,"is a hexadecimal number!!!")  

if __name__ == "__main__":
    main()
