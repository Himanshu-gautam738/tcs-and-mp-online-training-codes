#include <stdio.h>
#include <ctype.h>
int main(int argc, char *argv[])
{
    int i, j, count = 0;
    for(i = 1; i < argc; i++)
    {
        for(j = 0; argv[i][j] != '\0'; j++)
        {
            if(isalnum(argv[i][j])) 
            {
                count++;
            }
        }
    }

    printf("Total characters = %d\n", count);

    return 0;
}
