def intro_msg():
    #Prints introduction message, prompts for input, and handles quit command.
    print("I can reverse a string.")
    print("If you give me 'apple', I will return 'elppa'.")
    print("I can even do an entire sentence.")
    while True:
        user_input = input("Type something and see or type 'quit' to exit: ")
        if user_input.lower() == "quit":
            break
        return user_input

def reverse_word(characters):
    #Reverses a given string using a while loop.
    reverse_string = ""
    while characters:
        last_char = characters[-1]
        reverse_string += last_char
        characters = characters[:-1]
    return reverse_string

def main():
    #Main loop to print reversed strings until user quits.
    while True:
        word = intro_msg()
        if word is None:  # Exit if user types 'quit'
            break
        reversed_word = reverse_word(word)
        print(f"\nBelow is your string in reverse:\n{reversed_word}")

if __name__ == "__main__":
    main()
