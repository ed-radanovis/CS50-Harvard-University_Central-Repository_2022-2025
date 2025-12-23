#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      // Calculate average of red, green, and blue
      int avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

      // Set all channels to the average value
      image[i][j].rgbtRed = avg;
      image[i][j].rgbtGreen = avg;
      image[i][j].rgbtBlue = avg;
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
      // Swap pixels from left and right sides
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
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      temp[i][j] = image[i][j];
    }
  }

  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      int sumRed = 0, sumGreen = 0, sumBlue = 0;
      int count = 0;

      // Check the 3x3 neighborhood
      for (int di = -1; di <= 1; di++)
      {
        for (int dj = -1; dj <= 1; dj++)
        {
          int ni = i + di;
          int nj = j + dj;

          // Check if within bounds
          if (ni >= 0 && ni < height && nj >= 0 && nj < width)
          {
            sumRed += temp[ni][nj].rgbtRed;
            sumGreen += temp[ni][nj].rgbtGreen;
            sumBlue += temp[ni][nj].rgbtBlue;
            count++;
          }
        }
      }

      // Assign the average values
      image[i][j].rgbtRed = round((float)sumRed / count);
      image[i][j].rgbtGreen = round((float)sumGreen / count);
      image[i][j].rgbtBlue = round((float)sumBlue / count);
    }
  }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
  // Create a temporary copy of the image
  RGBTRIPLE temp[height][width];
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      temp[i][j] = image[i][j];
    }
  }

  // Sobel kernels
  int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
  int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      int Gx_red = 0, Gx_green = 0, Gx_blue = 0;
      int Gy_red = 0, Gy_green = 0, Gy_blue = 0;

      // Check the 3x3 neighborhood
      for (int di = -1; di <= 1; di++)
      {
        for (int dj = -1; dj <= 1; dj++)
        {
          int ni = i + di;
          int nj = j + dj;

          // If out of bounds, treat as black (0)
          int red = 0, green = 0, blue = 0;
          if (ni >= 0 && ni < height && nj >= 0 && nj < width)
          {
            red = temp[ni][nj].rgbtRed;
            green = temp[ni][nj].rgbtGreen;
            blue = temp[ni][nj].rgbtBlue;
          }

          // Multiply by Sobel kernel values
          Gx_red += red * Gx[di + 1][dj + 1];
          Gx_green += green * Gx[di + 1][dj + 1];
          Gx_blue += blue * Gx[di + 1][dj + 1];

          Gy_red += red * Gy[di + 1][dj + 1];
          Gy_green += green * Gy[di + 1][dj + 1];
          Gy_blue += blue * Gy[di + 1][dj + 1];
        }
      }

      // Calculate the resulting value for each channel
      int red = round(sqrt(Gx_red * Gx_red + Gy_red * Gy_red));
      int green = round(sqrt(Gx_green * Gx_green + Gy_green * Gy_green));
      int blue = round(sqrt(Gx_blue * Gx_blue + Gy_blue * Gy_blue));

      // Cap values at 255
      image[i][j].rgbtRed = red > 255 ? 255 : red;
      image[i][j].rgbtGreen = green > 255 ? 255 : green;
      image[i][j].rgbtBlue = blue > 255 ? 255 : blue;
    }
  }
}