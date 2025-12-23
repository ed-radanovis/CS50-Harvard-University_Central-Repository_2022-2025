// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     string s = get_string("Input: ");
//     printf("Output: ");
//     for (int i = 0; s[i] != '\0'; i++)
//     {
//         printf("%c", s[i]);
//     }
//     printf("\n");
// }


// #include <cs50.h>
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
//     string s = get_string("Input: ");
//     printf("Output: ");
//     for (int i = 0; strlen(s); i++)    // => recurso (função) da biblioteca (string.h) que foi
//     {                                  //    criada para informar qual o comprimento da string.
//         printf("%c", s[i]);
//     }
//     printf("\n");
// }

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input: ");
    printf("Output: ");
    // int n = strlen(s);   => existe outro recurso sutil de loops FOR em C que permite
                            // introduzir esta variável dentro do laço. Conforme abaixo.
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}