#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{   //{"Jimmy", "Spencer", "Ozzy", "Eddy", "Jhon", "Bill", "David"};
    string names[] = {"Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"};

    for (int i = 0; i < 7; i++)
    {
        if (strcmp(names[i], "Ron") == 0)  // We cannot compare strings directly in C, as they are not a
                                      // simple data type, but rather an array of many characters.
                                      // Fortunately, the string library has a strcmp ("string compare")
                                      // function that compares strings for nodes, one character at a time, and returns 0 if they match.
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
            return 1;
}