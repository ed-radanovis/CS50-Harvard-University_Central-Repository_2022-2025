from cs50 import get_int


def main():
    # Get card number from user
    card_number = get_int("Number: ")

    # Validate using Luhn's algorithm
    if not luhn_algorithm(card_number):
        print("INVALID")
        return 0

    # Get card length and starting digits
    length = get_length(card_number)
    start_digits = get_start_digits(card_number, length)

    # Print card type
    print_card_type(start_digits, length)


def luhn_algorithm(card_number):
    """Implements Luhn's algorithm for credit card validation"""
    sum = 0
    alternate = False

    while card_number > 0:
        digit = card_number % 10

        if alternate:
            digit *= 2
            sum += (digit // 10) + (digit % 10)
        else:
            sum += digit

        alternate = not alternate
        card_number //= 10

    return sum % 10 == 0


def get_length(number):
    """Returns number of digits in the card number"""
    length = 0
    while number > 0:
        number //= 10
        length += 1
    return length


def get_start_digits(number, length):
    """Returns first two digits of the card number"""
    for i in range(length - 2):
        number //= 10
    return number


def print_card_type(start_digits, length):
    """Determines and prints the card type"""
    # American Express (15 digits, starts with 34 or 37)
    if length == 15 and (start_digits == 34 or start_digits == 37):
        print("AMEX")
    # MasterCard (16 digits, starts with 51-55)
    elif length == 16 and (51 <= start_digits <= 55):
        print("MASTERCARD")
    # Visa (13 or 16 digits, starts with 4)
    elif (length == 13 or length == 16) and (start_digits // 10 == 4):
        print("VISA")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()

# # credit.py => native to Python (without the CS50 library):


# def main():
#     # Get card number from user as string
#     card_str = input("Number: ")

#     # Remove any spaces or dashes
#     card_str = card_str.replace(" ", "").replace("-", "")

#     # Validate input is numeric
#     if not card_str.isdigit():
#         print("INVALID")
#         return

#     # Convert to integer for calculations
#     card_number = int(card_str)

#     # Validate using Luhn's algorithm
#     if not luhn_algorithm(card_number):
#         print("INVALID")
#         return

#     # Get card length and starting digits
#     length = len(card_str)  # More efficient than get_length function
#     start_digits = int(card_str[:2])

#     # Print card type
#     print_card_type(start_digits, length)


# def luhn_algorithm(card_number):
#     """Implements Luhn's algorithm for credit card validation"""
#     sum = 0
#     alternate = False

#     while card_number > 0:
#         digit = card_number % 10

#         if alternate:
#             digit *= 2
#             sum += (digit // 10) + (digit % 10)
#         else:
#             sum += digit

#         alternate = not alternate
#         card_number //= 10

#     return sum % 10 == 0


# def print_card_type(start_digits, length):
#     """Determines and prints the card type"""
#     # American Express (15 digits, starts with 34 or 37)
#     if length == 15 and start_digits in [34, 37]:
#         print("AMEX")
#     # MasterCard (16 digits, starts with 51-55)
#     elif length == 16 and 51 <= start_digits <= 55:
#         print("MASTERCARD")
#     # Visa (13 or 16 digits, starts with 4)
#     elif length in [13, 16] and str(start_digits).startswith("4"):
#         print("VISA")
#     else:
#         print("INVALID")


# if __name__ == "__main__":
#     main()
