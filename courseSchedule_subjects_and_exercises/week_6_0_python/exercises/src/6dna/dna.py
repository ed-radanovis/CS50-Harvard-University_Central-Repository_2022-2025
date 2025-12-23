import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    dna_file = sys.argv[2]

    # Read database CSV file
    with open(database_file, "r") as db_file:
        reader = csv.DictReader(db_file)
        database = list(reader)

    # Read DNA sequence file into a variable
    with open(dna_file, "r") as seq_file:
        dna_sequence = seq_file.read().strip()

    # Extract STR names from database (excluding 'name' column)
    str_names = list(database[0].keys())[1:]  # Skip the 'name' field

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_name in str_names:
        str_counts[str_name] = longest_match(dna_sequence, str_name)

    # Check database for matching profiles
    match_found = False
    for person in database:
        # Check if all STR counts match for this person
        match = True
        for str_name in str_names:
            # Convert STR count from database to integer for comparison
            if int(person[str_name]) != str_counts[str_name]:
                match = False
                break

        if match:
            print(person["name"])
            match_found = True
            break

    # If no match found
    if not match_found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
