from cs50 import get_float


def main():
    """Main program to calculate and display minimum coins"""
    # Get valid change amount in dollars from user
    dollars = get_dollars()

    # Convert dollars to cents to avoid floating-point issues
    cents = round(dollars * 100)

    # Calculate minimum coins using greedy algorithm
    coins = calculate_coins(cents)

    # Display result (just the number on its own line)
    print(coins)


def get_dollars():
    """
    Prompts user for non-negative dollar amount
    Returns: float dollar amount
    """
    while True:
        dollars = get_float("Change: ")
        if dollars >= 0:
            return dollars
        print("Amount must be non-negative.")


def calculate_coins(cents):
    """
    Calculates minimum coins using greedy algorithm
    Args: cents - integer amount in cents
    Returns: total number of coins needed
    """
    # Coin denominations in descending order
    denominations = [25, 10, 5, 1]
    coin_count = 0

    # Use each coin type greedily
    for coin_value in denominations:
        coin_count += cents // coin_value  # Integer division
        cents %= coin_value  # Remainder after using this coin type

    return coin_count


# Alternative: More explicit version
def calculate_coins_explicit(cents):
    """
    Explicit calculation similar to C version
    More readable for those familiar with original problem
    """
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return quarters + dimes + nickels + pennies


# Alternative: Using while loops
def calculate_coins_while(cents):
    """
    Alternative using while loops for each coin type
    """
    coins = 0

    # Quarters
    while cents >= 25:
        cents -= 25
        coins += 1

    # Dimes
    while cents >= 10:
        cents -= 10
        coins += 1

    # Nickels
    while cents >= 5:
        cents -= 5
        coins += 1

    # Pennies
    while cents >= 1:
        cents -= 1
        coins += 1

    return coins


# Execute program
if __name__ == "__main__":
    main()

# # cash.py => native to Python (without the CS50 library):


# def main():
#     dollars = get_dollars()
#     cents = round(dollars * 100)

#     coins = 0
#     for denom in (25, 10, 5, 1):
#         coins += cents // denom
#         cents %= denom

#     print(coins)


# def get_dollars():
#     while True:
#         try:
#             dollars = float(input("Change: "))
#             if dollars >= 0:
#                 return dollars
#             print("Amount must be non-negative.")
#         except ValueError:
#             print("Please enter a valid number.")


# if __name__ == "__main__":
#     main()
