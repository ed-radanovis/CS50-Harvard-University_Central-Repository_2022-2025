#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long x = get_long("x: ");  //get_long suporta números até 64 BITS ou 8.000.000.000

    int y = get_long("y: ");

    printf("%li\n", x + y);
}