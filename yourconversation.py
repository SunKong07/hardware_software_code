def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input().lower().strip()
    if answer == "yes":
        print("That's good - the United States needs more coders!!")
    elif answer == "no":
        print("Perhaps you will change your mind ")
    else:
        print("I don't understand?")
        print("Goodbye")
def main():
    print("Welcome to my conversation program")
    conversation()
    print("Thanks for chatting with me")

if __name__ == "__main__":
    main()
