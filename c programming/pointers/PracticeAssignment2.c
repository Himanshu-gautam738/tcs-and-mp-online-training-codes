#include <stdio.h>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
int sumArray(int *arr, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += *(arr + i);
    }
    return sum;
}
void displayArray(int *arr, int size)
{
    printf("Array elements: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}
int main()
{
    int a = 10, b = 20;
    int arr[5] = {1, 2, 3, 4, 5};
    int *ptr1, *ptr2;
    ptr1 = &a;
    ptr2 = &b;
    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(ptr1, ptr2);
    printf("After swap:  a = %d, b = %d\n", a, b);

    displayArray(arr, 5);
    printf("Sum of array elements = %d\n", sumArray(arr, 5));
    int *p = arr;
    printf("First element: %d\n", *p);
    p++;
    printf("Second element using pointer arithmetic: %d\n", *p);

    return 0;
}
