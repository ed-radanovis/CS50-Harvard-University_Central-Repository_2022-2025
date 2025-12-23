#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function prototypes
bool is_valid_key(string key);
char substitute(char c, string key);

int main(int argc, string argv[])
{
  // Checking if the number of arguments is correct
  if (argc != 2)
  {
    printf("Usage: ./substitution key\n");
    return 1;
  }

  string key = argv[1];

  // Validate the key
  if (!is_valid_key(key))
  {
    return 1;
  }

  // Get plaintext from user
  string plaintext = get_string("plaintext: ");

  // Print ciphertext header
  printf("ciphertext: ");

  // Encrypt each character
  for (int i = 0, n = strlen(plaintext); i < n; i++)
  {
    printf("%c", substitute(plaintext[i], key));
  }

  // Newline at the end
  printf("\n");

  return 0;
}

// Function to validate the key
bool is_valid_key(string key)
{
  int length = strlen(key);

  // Check if key has 26 characters
  if (length != 26)
  {
    printf("Key must contain 26 characters.\n");
    return false;
  }

  // Array to track which letters we've seen (case-insensitive)
  bool seen[26] = {false};

  for (int i = 0; i < length; i++)
  {
    // Check if character is alphabetic
    if (!isalpha(key[i]))
    {
      printf("Key must contain only alphabetic characters.\n");
      return false;
    }

    // Convert to uppercase index (0-25)
    int index = toupper(key[i]) - 'A';

    // Check if this letter has been seen before
    if (seen[index])
    {
      printf("Key must not contain repeated characters.\n");
      return false;
    }

    // Mark this letter as seen
    seen[index] = true;
  }

  return true;
}

// Function to substitute a character using the key
char substitute(char c, string key)
{
  // If character is uppercase
  if (isupper(c))
  {
    // Convert to index (0-25), get corresponding key character, keep uppercase
    int index = c - 'A';
    return toupper(key[index]);
  }
  // If character is lowercase
  else if (islower(c))
  {
    // Convert to index (0-25), get corresponding key character, keep lowercase
    int index = c - 'a';
    return tolower(key[index]);
  }
  // If character is not alphabetic, return unchanged
  else
  {
    return c;
  }
}