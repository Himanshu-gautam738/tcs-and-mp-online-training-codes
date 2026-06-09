#include <stdio.h>

void swapInt(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int compareInt(int a, int b) {
    return a > b;   // return 1 if first is greater
}

void quickSortInt(int arr[], int low, int high, int (*cmp)(int, int)) {
    if (low >= high)
        return;

    int pivot = arr[(low + high) / 2];
    int i = low, j = high;

    while (i <= j) {
        while (cmp(pivot, arr[i])) i++;
        while (cmp(arr[j], pivot)) j--;
        if (i <= j) {
            swapInt(&arr[i], &arr[j]);
            i++;
            j--;
        }
    }

    if (low < j) quickSortInt(arr, low, j, cmp);
    if (i < high) quickSortInt(arr, i, high, cmp);
}

void printIntArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {5, 2, 9, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array:\n");
    printIntArray(arr, n);

    quickSortInt(arr, 0, n - 1, compareInt);

    printf("Sorted array:\n");
    printIntArray(arr, n);

    return 0;
}
