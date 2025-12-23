#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_double_pyramid(int height);

int main(void)
{
  // Get height of pyramid
  int height = get_height();

  // Print double pyramid
  print_double_pyramid(height);
}

// Prompt user for height between 1 and 8
int get_height(void)
{
  int height;
  do
  {
    height = get_int("Height: ");
  } while (height < 1 || height > 8);
  return height;
}

// Print double pyramid with gap
void print_double_pyramid(int height)
{
  for (int row = 0; row < height; row++)
  {
    // Left pyramid spaces
    for (int space = 0; space < height - row - 1; space++)
    {
      printf(" ");
    }

    // Left pyramid hashes
    for (int hash = 0; hash < row + 1; hash++)
    {
      printf("#");
    }

    // Gap (2 spaces)
    printf("  ");

    // Right pyramid hashes
    for (int hash = 0; hash < row + 1; hash++)
    {
      printf("#");
    }

    // New line
    printf("\n");
  }
}