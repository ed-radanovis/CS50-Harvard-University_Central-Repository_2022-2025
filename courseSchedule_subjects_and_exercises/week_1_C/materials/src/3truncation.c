/* #include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get numbers from user
    int x = get_int("x: ");             NÃO RECONHECE OS DECIMAIS POR CAUSA DO (int)
    int y = get_int("y: ");

    // Divide x by y
    float z = x / y;
    printf("%f\n", z);
} */

/* #include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get numbers from user
    float x = get_float("x: ");         RECONHECE OS DECIMAIS POR CAUSA DO (float)
    float y = get_float("y: ");         PORÉM SOLUÇÃO PESADA POR TER QUE ALTERAR TODO O CÓDIGO

    // Divide x by y
    float z = x / y;
    printf("%f\n", z);
}*/
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get numbers from user
    int x = get_int("x: ");
    int y = get_int("y: ");

    // Divide x by y
    float z = (float)x / (float)y;     // <= então usando o CASTING, conforme ex. estaremos dizendo que o
    printf("%f\n", z);                 //    'x' e o 'y' são na 'n,0' ou seja decimais por conta do (float).
}