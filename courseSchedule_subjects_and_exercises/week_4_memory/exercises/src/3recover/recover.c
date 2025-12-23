#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
  // Check for exactly one command-line argument
  if (argc != 2)
  {
    printf("Usage: ./recover FILE\n");
    return 1;
  }

  // Open the forensic image file
  FILE *card = fopen(argv[1], "r");
  if (card == NULL)
  {
    printf("Could not open %s.\n", argv[1]);
    return 1;
  }

  // Buffer to store 512-byte blocks
  uint8_t buffer[BLOCK_SIZE];

  // Variables for JPEG file management
  FILE *jpeg = NULL;
  int file_count = 0;
  bool found_jpeg = false;

  // Read the file block by block
  while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
  {
    // Check if this is the start of a new JPEG
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
        (buffer[3] & 0xf0) == 0xe0)
    {
      // If we already have a JPEG open, close it
      if (found_jpeg)
      {
        fclose(jpeg);
      }
      else
      {
        found_jpeg = true;
      }

      // Create the filename for the new JPEG
      char filename[8]; // 000.jpg\0 = 8 characters
      sprintf(filename, "%03d.jpg", file_count);
      file_count++;

      // Open the new JPEG file for writing
      jpeg = fopen(filename, "w");
      if (jpeg == NULL)
      {
        printf("Could not create %s.\n", filename);
        fclose(card);
        return 1;
      }
    }

    // If we're currently inside a JPEG, write this block to it
    if (found_jpeg)
    {
      fwrite(buffer, 1, BLOCK_SIZE, jpeg);
    }
  }

  // Close any open files
  if (found_jpeg)
  {
    fclose(jpeg);
  }
  fclose(card);

  return 0;
}