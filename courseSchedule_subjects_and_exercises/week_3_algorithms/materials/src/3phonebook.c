// #include <cs50.h>
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
//     string names[] = {"Bill", "Charlie"};
//     string numbers[] = {"(35) 9-8433-2466", "(11) 9-9965-6969"};

//     for (int i = 0; i < 2; i++)
//     {
//         if (strcmp(names[i], "Bill") == 0)
//         {
//             printf("Found%s\n", numbers[i]);
//             return 0;
//         }
//     }
//     printf("Not found\n");
//             return 1;
// }

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
 string name;
 string number;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "Bill";
    people[0].number = "(35) 9-8433-2466";

    people[1].name = "Charlie";
    people[1].number = "(11) 9-9965-6969";

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, "Bill") == 0)
        {
            printf("Found%s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
            return 1;
}