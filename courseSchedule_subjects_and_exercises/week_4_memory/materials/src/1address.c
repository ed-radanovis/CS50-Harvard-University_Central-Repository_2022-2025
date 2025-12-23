// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     printf("%p\n", &n);
// }

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     printf("%i\n", *&n);
// }

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n;
//     printf("%p\n", p);
// }

// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!";
//     printf("%p\n", &s[0]);
//     printf("%p\n", &s[1]);
//     printf("%p\n", &s[2]);
// }

// #include <stdio.h>

// int main(void)
// {
//     char *s = "HI!";
//     printf("%c\n", s[0]);
//     printf("%c\n", s[1]);
//     printf("%c\n", s[2]);
// }

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%i\n", *(s+3));
}