/*#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("Edmar\n");
    }
}       => depois desse exemplo ele cria um com função conforme abaixo*/

/*#include <cs50.h>
#include <stdio.h>

void edmar(void)
{
    printf("Ed BONITÃO\n");
}

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        edmar();
    }
}       => obs. por convenção normalmente colacam-se as funções personalizadas
           na parte inferior do arquivo conforme exemplo abaixo. */

#include <cs50.h>
#include <stdio.h>

// (*) Prototype
void edmar(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        edmar();
    }
}

void edmar(void)
{
    printf("Ed BONITÃO\n");
}                                    // => porém qd executado dessa maneira criam-se 2 bugs
                                     //    (*) e a solução para isto é simplesmente copiar a 1ª linha da função
                                     //        e colar no topo do arquivo com (;) acima do MAIN (nota:função principal).
                                     //        Esta solução chama-se PROTOTYPE que uma forma de dizer ao compilador de
                                     //        que existirá uma função chamada (...), mas ela ainda não existe.