#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

// Function declaration
void readability(string text);

int main(void)
{
  // Get text from user
  string text = get_string("Text: ");
  readability(text);
}

void readability(string text)
{
  int letters = 0;
  int words = 0;
  int sentences = 0;
  int length = strlen(text);

  // Edge case: empty string
  if (length == 0)
  {
    printf("Before Grade 1\n");
    return;
  }

  // Track if we're inside a word to handle multiple spaces
  bool in_word = false;

  // Check all characters of the received text
  for (int i = 0; i < length; i++)
  {
    // Check if the character is a letter
    if (isalpha(text[i]))
    {
      letters++;
      if (!in_word)
      {
        words++;
        in_word = true;
      }
    }
    // Check if the character is a space
    else if (isspace(text[i]))
    {
      in_word = false;
    }
    // Check if the character is sentence-ending punctuation
    else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
    {
      sentences++;
      in_word = false;
    }
    // For other characters (like numbers, commas, etc.), stay in word if we were in one
    else
    {
      if (!in_word)
      {
        words++;
        in_word = true;
      }
    }
  }

  // Calculate L and S for Coleman-Liau formula
  // L = average number of letters per 100 words
  // S = average number of sentences per 100 words
  float L = (letters / (float)words) * 100;
  float S = (sentences / (float)words) * 100;

  // Coleman-Liau formula
  int index = round(0.0588 * L - 0.296 * S - 15.8);

  // Output result according to specifications
  if (index < 1)
  {
    printf("Before Grade 1\n");
  }
  else if (index >= 16)
  {
    printf("Grade 16+\n");
  }
  else
  {
    printf("Grade %i\n", index);
  }
}