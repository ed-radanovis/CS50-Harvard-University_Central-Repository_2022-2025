from cs50 import get_string
import math


def main():
    # Get text from user
    text = get_string("Text: ")
    readability(text)


def readability(text):
    letters = 0
    words = 0
    sentences = 0
    length = len(text)

    # Edge case: empty string
    if length == 0:
        print("Before Grade 1")
        return

    # Track if we're inside a word to handle multiple spaces
    in_word = False

    # Check all characters of the received text
    for i in range(length):
        # Check if the character is a letter
        if text[i].isalpha():
            letters += 1
            if not in_word:
                words += 1
                in_word = True
        # Check if the character is a space
        elif text[i].isspace():
            in_word = False
        # Check if the character is sentence-ending punctuation
        elif text[i] in [".", "?", "!"]:
            sentences += 1
            in_word = False
        # For other characters (like numbers, commas, etc.), stay in word if we were in one
        else:
            if not in_word:
                words += 1
                in_word = True

    # Handle edge case where text ends without punctuation
    if words == 0:
        print("Before Grade 1")
        return

    # Calculate L and S for Coleman-Liau formula
    # L = average number of letters per 100 words
    # S = average number of sentences per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Coleman-Liau formula
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Output result according to specifications
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()


# # readability.py => native to Python (without the CS50 library):

# import math


# def main():
#     # Get text from user
#     text = input("Text: ")
#     readability(text)


# def readability(text):
#     letters = 0
#     words = 0
#     sentences = 0
#     length = len(text)

#     # Edge case: empty string
#     if length == 0:
#         print("Before Grade 1")
#         return

#     # Track if we're inside a word to handle multiple spaces
#     in_word = False

#     # Check all characters of the received text
#     for char in text:
#         # Check if the character is a letter
#         if char.isalpha():
#             letters += 1
#             if not in_word:
#                 words += 1
#                 in_word = True
#         # Check if the character is a space
#         elif char.isspace():
#             in_word = False
#         # Check if the character is sentence-ending punctuation
#         elif char in [".", "?", "!"]:
#             sentences += 1
#             in_word = False
#         # For other characters (like numbers, commas, etc.), stay in word if we were in one
#         else:
#             if not in_word:
#                 words += 1
#                 in_word = True

#     # Handle edge case where text ends without punctuation
#     if words == 0:
#         print("Before Grade 1")
#         return

#     # Calculate L and S for Coleman-Liau formula
#     # L = average number of letters per 100 words
#     # S = average number of sentences per 100 words
#     L = (letters / words) * 100
#     S = (sentences / words) * 100

#     # Coleman-Liau formula
#     index = round(0.0588 * L - 0.296 * S - 15.8)

#     # Output result according to specifications
#     if index < 1:
#         print("Before Grade 1")
#     elif index >= 16:
#         print("Grade 16+")
#     else:
#         print(f"Grade {index}")


# if __name__ == "__main__":
#     main()
