def decimal_to_binary(selection):
    result = ""
    number = int(selection)
    while number > 0:                 #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  #place string in reverse order
    return result

def check_selection(numbers): #verify if it is a decimal
    dec_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() not in dec_list:  # check if the number is not in dec list
            print( number,"is not a decimal number")
            return(False)
    return(True)

def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a decimal number:")
        good_selection = check_selection(selection)
    print("Good job", selection, "is decimal number!!!")
    print("There for decimal {} to binary: {}".format(selection, decimal_to_binary(selection)))

if __name__ == "__main__":
    main() #add check for valid numbers
