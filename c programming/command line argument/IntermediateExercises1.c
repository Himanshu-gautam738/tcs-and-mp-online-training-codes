#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int i;
    int maxLen = 0;
    int index = -1;

    if (argc <= 1)
    {
        printf("No command-line arguments provided.\n");
        return 0;
    }

    for (i = 1; i < argc; i++)
    {
        int len = strlen(argv[i]);
        if (len > maxLen)
        {
            maxLen = len;
            index = i;
        }
    }

    printf("Longest argument: %s\n", argv[index]);
    return 0;
}
