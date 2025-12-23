#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
  char word[LENGTH + 1];
  struct node *next;
} node;

// Choose number of buckets in hash table (prime number for better distribution)
const unsigned int N = 200003; // Larger prime number for fewer collisions

// Hash table
node *table[N];

// Counter for dictionary size
unsigned int word_count = 0;

// Hashes word to a number (djb2 hash function)
unsigned int hash(const char *word)
{
  // Source: http://www.cse.yorku.ca/~oz/hash.html
  unsigned long hash = 5381;
  int c;

  while ((c = *word++))
  {
    hash = ((hash << 5) + hash) + tolower(c); // hash * 33 + c
  }

  return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
  // Open dictionary file
  FILE *file = fopen(dictionary, "r");
  if (file == NULL)
  {
    return false;
  }

  // Buffer for reading words
  char word[LENGTH + 1];

  // Read words from file one at a time
  while (fscanf(file, "%s", word) != EOF)
  {
    // Create a new node
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
      fclose(file);
      return false;
    }

    // Copy word into node
    strcpy(n->word, word);

    // Hash word to get index
    unsigned int index = hash(word);

    // Insert node at beginning of linked list
    n->next = table[index];
    table[index] = n;

    // Increment word count
    word_count++;
  }

  // Close dictionary file
  fclose(file);
  return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
  // Hash word to get index
  unsigned int index = hash(word);

  // Traverse linked list at that index
  for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
  {
    // Compare strings case-insensitively
    if (strcasecmp(cursor->word, word) == 0)
    {
      return true;
    }
  }

  return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
  return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
  // Iterate through all buckets
  for (unsigned int i = 0; i < N; i++)
  {
    // Free linked list at each bucket
    while (table[i] != NULL)
    {
      node *tmp = table[i]->next;
      free(table[i]);
      table[i] = tmp;
    }
  }

  return true;
}