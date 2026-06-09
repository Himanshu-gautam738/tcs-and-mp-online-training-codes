#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Enter two numbers!\n");
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    printf("A=%d  B=%d\n", a, b);
    printf("AND=%d\n", a & b);
    printf("OR=%d\n", a | b);
    printf("XOR=%d\n", a ^ b);
    printf("NOT A=%d\n", ~a);
    printf("A<<1=%d\n", a << 1);
    printf("A>>1=%d\n", a >> 1);

    return 0;
}
