from cs50 import get_int


def main():
    # Get pyramid height from user
    height = get_height()

    # Print the double pyramid
    print_double_pyramid(height)


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


def print_double_pyramid(height):
    """Prints two half pyramids with specified height and 2-space gap"""
    for row in range(height):
        # Print spaces for left pyramid alignment
        for space in range(height - row - 1):
            print(" ", end="")

        # Print left pyramid hashes
        for hash in range(row + 1):
            print("#", end="")

        # Print 2-space gap between pyramids
        print("  ", end="")

        # Print right pyramid hashes
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

#     # Print the double pyramid
#     print_double_pyramid(height)


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


# def print_double_pyramid(height):
#     """Prints two half pyramids with specified height and 2-space gap"""
#     for row in range(height):
#         # Calculate components for this row
#         spaces = " " * (height - row - 1)
#         hashes = "#" * (row + 1)

#         # Print the complete row: spaces + left hashes + gap + right hashes
#         print(f"{spaces}{hashes}  {hashes}")


# if __name__ == "__main__":
#     main()
