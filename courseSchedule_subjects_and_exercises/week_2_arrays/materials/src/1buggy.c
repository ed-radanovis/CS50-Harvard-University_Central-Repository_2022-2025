#include <cs50.h>
#include <stdio.h>

// Prototype
int get_negative_int(void);

int main(void)
{
    // Get a negative integer from user
    int i = get_negative_int();
    printf ("%i \n", i);
}

int get_negative_int(void)
{
    int n;
    do
    {
         n = get_int ("Negative integer:");
    }
    while (n < 0); // so, after i have use debug50 discovery that the problem would be solved with this "while (n >= 0);"
    return n;
}