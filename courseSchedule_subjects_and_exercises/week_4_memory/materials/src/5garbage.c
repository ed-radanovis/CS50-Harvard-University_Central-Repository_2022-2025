// int main(void)
// {
//     int *x;
//     int *y;
//     x = malloc(sizeof(int));
//     *x = 42;
//     *y = 13;
//     y = x;
//     *y = 13;
// }

#include <stdio.h>

int main(void)
{
    int scores[3];
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", scores[i]);
    }
}