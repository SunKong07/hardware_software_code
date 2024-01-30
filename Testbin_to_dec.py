def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1 #determine greatest power
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1    # decrease by 1
        return result

def main():
    num = input("Enter Binary Number:")
    print("Binary {0} is equal to Decimal: {1}".format(num, binary_to_decimal(num)))

if __name__ == "__main__":
    main()
