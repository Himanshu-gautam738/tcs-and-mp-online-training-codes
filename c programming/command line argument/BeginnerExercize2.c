#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    if (argc <= 1)
    {
        printf("No command-line arguments provided.\n");
        return 0;
    }

    printf("Arguments in reverse order:\n");

    for (i = argc - 1; i >= 1; i--)   //reverse input
    {
        printf("%s\n", argv[i]);
    }

    return 0;
}
