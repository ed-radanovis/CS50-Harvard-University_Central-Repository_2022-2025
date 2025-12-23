from cs50 import get_int


def main():
    # Get pyramid height from user
    height = get_height()

    # Print the pyramid
    print_pyramid(height)


def get_height():
    """Prompts user for height between 1 and 8, inclusive"""
    while True:
        try:
            height = get_int("Height: ")
            if 1 <= height <= 8:
                return height
            else:
                print("Height must be between 1 and 8, inclusive.")
        except ValueError:
            print("Please enter a valid integer.")


def print_pyramid(height):
    """Prints a half pyramid with specified height"""
    for row in range(height):
        # Print spaces for right alignment
        for space in range(height - row - 1):
            print(" ", end="")

        # Print hashes for pyramid blocks
        for hash in range(row + 1):
            print("#", end="")

        # Move to next line
        print()


if __name__ == "__main__":
    main()


# mario.py => native to Python (without the CS50 library):


# def main():
#     # Get pyramid height from user
#     height = get_height()

#     # Print the pyramid
#     print_pyramid(height)


# def get_height():
#     """Prompts user for height between 1 and 8, inclusive"""
#     while True:
#         try:
#             height = int(input("Height: "))
#             if 1 <= height <= 8:
#                 return height
#             else:
#                 print("Height must be between 1 and 8, inclusive.")
#         except ValueError:
#             print("Please enter a valid integer.")


# def print_pyramid(height):
#     """Prints a half pyramid with specified height"""
#     for row in range(height):
#         # Print spaces and hashes using string multiplication
#         print(" " * (height - row - 1) + "#" * (row + 1))


# if __name__ == "__main__":
#     main()
