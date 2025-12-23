// #include <cs50.h>
// #include <stdio.h>

// int main(int argc, string argv[]) // => ARGC abreviação de argument count (contagem de argumentos), ou seja é o nº inteiro que vai representar o nº de palavras
// {                                 //    que seus usuários digitam no prompt, e ARGV abreviação de argument vector (vetor (lista) de argumento) ou seja é uma
//     if (argc == 2)                //    variável que irá armazenar em um array todas as strings que serão digitadas no prompt após o nome do seu próprio programa.
//     {
//         printf("Hello, %s\n", argv[1]);
//     }
//     else
//     {
//         printf("Hello, World\n");
//     }
// }

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[]) // => ARGC abreviação de argument count (contagem de argumentos), ou seja é o nº inteiro que vai representar o nº de palavras
{                                 //    que seus usuários digitam no prompt, e ARGV abreviação de argument vector (vetor (lista) de argumento) ou seja é uma
    if (argc == 2)                //    variável que irá armazenar em um array todas as strings que serão digitadas no prompt após o nome do seu próprio programa.
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            printf("%c\n", argv[1][i]);
        }
    }
}