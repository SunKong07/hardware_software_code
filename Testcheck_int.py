def check_user_input(chk_input): # verify that the number is an integer
    try:
        return int(chk_input)
    except:
        print("Invalid input")
        return False

def get_smallest(smallest, value):
    if smallest is None:
        largest = "because no number set"
        smallest = value
    elif value < smallest:
        largest = '{} {}'.format('than', smallest)
        smallest = value
    else:
        largest = '{} {}'.format('than', value)
    return (largest, smallest)

def main():
    make_selection = True
    while make_selection:
        selection = input("Select a whole number from:")
        make_selection, selection = check_user_input(selection)
    print("Good job", selection, "is a whole number!!!")

if __name__ == "__main__":
    main()
