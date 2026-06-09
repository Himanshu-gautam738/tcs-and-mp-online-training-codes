#include <stdio.h>

int main() {
    float f = 3.14;
    int *iptr = (int*)&f;   // Typecast float address to int pointer

    printf("Float value: %f\n", f);
    printf("Value interpreted as int: %d\n", *iptr);

    return 0;
}
