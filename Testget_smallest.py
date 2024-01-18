def get_smallest(smallest, value):
    if smallest is None:
        largest = "because no number set"
        smallest = value
    elif int(value) < int(smallest):
        largest = smallest
        smallest = value
    else:
        largest = value
    return (largest, smallest)

def main():
    smallest = None
    while True:
        num = input("Enter a number: ").lower()
        if num =="done":
            break
        largest, smallest = get_smallest(smallest, num)
        print(smallest, "is smaller", largest)

if __name__ == "__main__":
    main()
