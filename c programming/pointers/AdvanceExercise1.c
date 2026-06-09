#include <stdio.h>
#include <stdlib.h>

void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main() {
    int size = 5;
    int *a = NULL;
    a = (int *)malloc(size * sizeof(int));
    if (a == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    for (int i = 0; i < size; i++) {
        a[i] = i + 1;
    }
    printArray(a, size);
    free(a);
    return 0;
}
