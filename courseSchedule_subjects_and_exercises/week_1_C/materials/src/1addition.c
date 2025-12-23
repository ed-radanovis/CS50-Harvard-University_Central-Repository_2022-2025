#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x: "); //get_in suporta números até 32 BITS ou 4.000.000.000

    int y = get_int("y: ");

    printf("%i\n", x + y);
}
