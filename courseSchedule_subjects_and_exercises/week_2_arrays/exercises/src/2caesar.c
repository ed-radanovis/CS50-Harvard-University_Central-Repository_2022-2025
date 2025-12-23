#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// Function prototypes
char rotate(char c, int key);

int main(int argc, string argv[])
{
  // Checking if the number of arguments is correct
  if (argc != 2)
  {
    printf("Usage: ./caesar key\n");
    return 1;
  }

  // Check if all characters in the key are digits
  string key_string = argv[1];
  for (int i = 0, n = strlen(key_string); i < n; i++)
  {
    if (!isdigit(key_string[i]))
    {
      printf("Usage: ./caesar key\n");
      return 1;
    }
  }

  // Convert key to integer
  int key = atoi(key_string);

  // Get plaintext from user
  string plaintext = get_string("plaintext: ");

  // Print ciphertext header
  printf("ciphertext: ");

  // Encrypt each character
  for (int i = 0, n = strlen(plaintext); i < n; i++)
  {
    printf("%c", rotate(plaintext[i], key));
  }

  // Newline at the end
  printf("\n");

  return 0;
}

// Function to rotate a character by key positions
char rotate(char c, int key)
{
  // If character is uppercase
  if (isupper(c))
  {
    // Convert to 0-25 range, rotate, wrap around, convert back to ASCII
    return ((c - 'A' + key) % 26) + 'A';
  }
  // If character is lowercase
  else if (islower(c))
  {
    // Convert to 0-25 range, rotate, wrap around, convert back to ASCII
    return ((c - 'a' + key) % 26) + 'a';
  }
  // If character is not alphabetic, return unchanged
  else
  {
    return c;
  }
}