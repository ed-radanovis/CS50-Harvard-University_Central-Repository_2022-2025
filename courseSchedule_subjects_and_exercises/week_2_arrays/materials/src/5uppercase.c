// #include <cs50.h>
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
//     string s = get_string("Before: ");
//     printf("After: ");

//     for (int i = 0, n = strlen(s); i < n; i++)
//     {
//         if (s[i] >= 'a' && s[i] <= 'z')
//         {
//             printf("%c", s[i] -32);  // o nº 32 aqui representado refere-se a diferença entre as
//         }                            // letras maiúsculas e minúsculas em... Decimal ASCII Chart.
//         else
//         {
//             printf("%c", s[i]);
//         }
//     }
//     printf("\n");
// }


// #include <cs50.h>
// #include <ctype.h>  // outra biblioteca de linguagem C
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
//     string s = get_string("Before: ");
//     printf("After: ");

//     for (int i = 0, n = strlen(s); i < n; i++)
//     {
//         if (islower(s[i]))  //  => islower é uma função que retorna um valor booleano
//         {                   //     true or false, se esse caractere for minúsculo.
//             printf("%c", toupper(s[i]));
//         }
//         else
//         {
//             printf("%c", s[i]);
//         }
//     printf("\n");
// }

#include <cs50.h>
#include <ctype.h>  // outra biblioteca de linguagem C
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));       //  => simples representação de que o programador que criou a função
    }                                      //     (toupper) pensou em todas as possibilidades de aplicação dela.
                                           //      Que podemos representar o programa simplesmente assim!
    printf("\n");
}