#include <stdio.h>

int main(void)
{
    // i like'd to print ten hashs, but printed eleven
    for (int i = 0; i <= 10; i ++)
    {
          printf("# \n");
    }

    printf("\n");



    // Why???  With a simple printf, ...
    for (int i = 0; i <= 10; i ++)
    {
          printf("i is now %i\n",i);  // ... now, I can verify that it was started from zero
          printf("# \n");
    }
}
