#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}
#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      // Calculate average and round it
      float red = image[i][j].rgbtRed;
      float green = image[i][j].rgbtGreen;
      float blue = image[i][j].rgbtBlue;

      int average = round((red + green + blue) / 3);

      // Update pixel with average value
      image[i][j].rgbtRed = average;
      image[i][j].rgbtGreen = average;
      image[i][j].rgbtBlue = average;
    }
  }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      // Get original values
      float originalRed = image[i][j].rgbtRed;
      float originalGreen = image[i][j].rgbtGreen;
      float originalBlue = image[i][j].rgbtBlue;

      // Calculate sepia values
      int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
      int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
      int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

      // Cap at 255
      if (sepiaRed > 255)
        sepiaRed = 255;
      if (sepiaGreen > 255)
        sepiaGreen = 255;
      if (sepiaBlue > 255)
        sepiaBlue = 255;

      // Update pixel
      image[i][j].rgbtRed = sepiaRed;
      image[i][j].rgbtGreen = sepiaGreen;
      image[i][j].rgbtBlue = sepiaBlue;
    }
  }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width / 2; j++)
    {
      // Swap pixels from left and right
      RGBTRIPLE temp = image[i][j];
      image[i][j] = image[i][width - 1 - j];
      image[i][width - 1 - j] = temp;
    }
  }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  // Create a temporary copy of the image
  RGBTRIPLE temp[height][width];

  // Copy the original image to temp
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      temp[i][j] = image[i][j];
    }
  }

  // Apply blur to each pixel in the original image
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      int totalRed = 0, totalGreen = 0, totalBlue = 0;
      int count = 0;

      // Check all pixels in a 3x3 grid around current pixel
      for (int di = -1; di <= 1; di++)
      {
        for (int dj = -1; dj <= 1; dj++)
        {
          int newI = i + di;
          int newJ = j + dj;

          // Check if pixel is within image bounds
          if (newI >= 0 && newI < height && newJ >= 0 && newJ < width)
          {
            totalRed += temp[newI][newJ].rgbtRed;
            totalGreen += temp[newI][newJ].rgbtGreen;
            totalBlue += temp[newI][newJ].rgbtBlue;
            count++;
          }
        }
      }

      // Calculate average and update original image
      image[i][j].rgbtRed = round((float)totalRed / count);
      image[i][j].rgbtGreen = round((float)totalGreen / count);
      image[i][j].rgbtBlue = round((float)totalBlue / count);
    }
  }
}