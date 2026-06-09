#include <stdio.h>
#include <stdlib.h>

int countBits(int n)
{
    int c = 0;
    while (n)
    {
        c += n & 1;
        n >>= 1;
    }
    return c;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Enter numbers!\n");
        return 1;
    }
    int common = ~0, xorAll = 0;
    printf("\n--- Result ---\n");
    for (int i = 1; i < argc; i++)
    {
        int num = atoi(argv[i]);
        printf("%d -> %d\n", num, countBits(num));
        common &= num;
        xorAll ^= num;
    }
    printf("Common: %d\n", common);
    printf("XOR: %d\n", xorAll);
    return 0;
}
