#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p1 = NULL; // null pointer
    if (p1 != NULL)
    {
        *p1 = 10;
    }
    else
    {
        printf("p1 pointer is null\n");
    }
    int *p2; // Wild pointer
    int value = 20;
    p2 = &value;
    printf("p2 points to value: %d\n", *p2);

    int *p3 = (int *)malloc(sizeof(int));
    *p3 = 50;
    printf("Before free: *p3 = %d\n", *p3);
    free(p3);
    p3 = NULL;
    if (p3 == NULL)
        printf("After free: p3 set to null");

    return 0;
}
