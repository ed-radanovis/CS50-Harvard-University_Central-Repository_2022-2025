#include <cs50.h>
#include <stdio.h>

int get_start_size(void);
int get_end_size(int start_size);
int calculate_years(int start, int end);

int main(void)
{
  // Get start size
  int start = get_start_size();

  // Get end size
  int end = get_end_size(start);

  // Calculate number of years
  int years = calculate_years(start, end);

  // Print number of years
  printf("Years: %i\n", years);
}

// Prompt for start size (min 9)
int get_start_size(void)
{
  int start;
  do
  {
    start = get_int("Start size: ");
  } while (start < 9);
  return start;
}

// Prompt for end size (must be >= start size)
int get_end_size(int start_size)
{
  int end;
  do
  {
    end = get_int("End size: ");
  } while (end < start_size);
  return end;
}

// Calculate years required
int calculate_years(int start, int end)
{
  int years = 0;
  int population = start;

  while (population < end)
  {
    // Each year: population = population + born - died
    population = population + (population / 3) - (population / 4);
    years++;
  }

  return years;
}