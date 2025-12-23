/*#include <stdio.h>

int main(void)
{
     printf("????\n");
}
 => maneira simplificada de representar abaixo*/

/*#include <stdio.h>

int main(void)
{
    for (int i = 0; i <4; i++)
    {
    printf("?");
    }
    printf("\n");
}*/

/*#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get positive integer from user
    int n;
    do
    {
        n = get_int("Width: ");
    }
    while (n <1);

    // Print out that many question marks
    for (int i =0; i < n; i++)
    {
        printf("?");
    }
    printf("\n");
}*/

/*
imprimindo blocos bidimensionais
*/
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for(int i = 0; i < 3; i++)
    {
	    for(int j = 0; j < 3; j++)
    	{
         	printf("#");
    	}
    	printf("\n");
    }
}