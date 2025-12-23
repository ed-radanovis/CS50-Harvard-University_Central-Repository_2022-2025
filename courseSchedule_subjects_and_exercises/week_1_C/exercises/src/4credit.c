#include <cs50.h>
#include <stdio.h>

// Function prototypes
bool luhn_algorithm(long card_number);
int get_length(long number);
int get_start_digits(long number, int length);
void print_card_type(int start_digits, int length);

int main(void)
{
  // Get card number from user
  long card_number = get_long("Number: ");

  // Validate using Luhn's algorithm
  if (!luhn_algorithm(card_number))
  {
    printf("INVALID\n");
    return 0;
  }

  // Get card length and starting digits
  int length = get_length(card_number);
  int start_digits = get_start_digits(card_number, length);

  // Print card type
  print_card_type(start_digits, length);
}

// Implement Luhn's algorithm
bool luhn_algorithm(long card_number)
{
  int sum = 0;
  bool alternate = false;

  while (card_number > 0)
  {
    int digit = card_number % 10;

    if (alternate)
    {
      digit *= 2;
      sum += (digit / 10) + (digit % 10);
    }
    else
    {
      sum += digit;
    }

    alternate = !alternate;
    card_number /= 10;
  }

  return (sum % 10 == 0);
}

// Get number of digits
int get_length(long number)
{
  int length = 0;
  while (number > 0)
  {
    number /= 10;
    length++;
  }
  return length;
}

// Get first two digits
int get_start_digits(long number, int length)
{
  for (int i = 0; i < length - 2; i++)
  {
    number /= 10;
  }
  return number;
}

// Determine and print card type
void print_card_type(int start_digits, int length)
{
  // American Express (15 digits, starts with 34 or 37)
  if (length == 15 && (start_digits == 34 || start_digits == 37))
  {
    printf("AMEX\n");
  }
  // MasterCard (16 digits, starts with 51-55)
  else if (length == 16 && (start_digits >= 51 && start_digits <= 55))
  {
    printf("MASTERCARD\n");
  }
  // Visa (13 or 16 digits, starts with 4)
  else if ((length == 13 || length == 16) && (start_digits / 10 == 4))
  {
    printf("VISA\n");
  }
  else
  {
    printf("INVALID\n");
  }
}