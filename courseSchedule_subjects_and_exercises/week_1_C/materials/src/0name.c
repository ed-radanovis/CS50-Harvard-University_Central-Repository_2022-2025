#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("\n");
    string nome = get_string("Qual é seu nome? \n");
    printf("Olá, "" %s""!"" \n" ,nome);
    printf("\n");
}
