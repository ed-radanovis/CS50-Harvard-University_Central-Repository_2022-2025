#include <cs50.h>
#include <stdio.h>


int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument\n");
        return 1;
    }
    printf("Hello,%s\n", argv[1]);
    return 0;
}    // digitar no prompt o comando echo $?  para ver o status do retorno