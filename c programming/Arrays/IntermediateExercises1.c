/*Write a C program that takes an integer array and a shift value as input.
Implement a function to perform a circular shift on the array elements.*/

#include <stdio.h>
void circularShift(int arr[], int n)
{
    int temp, i;
    temp = arr[n - 1];      
    for (i = n - 1; i > 0; i--)
    {
        arr[i] = arr[i - 1]; 
    }
    arr[0] = temp;   
     printf("After circular shift:\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
}
int main()
{
    int arr[5], i;
    printf("Enter 5 elements:\n");
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }
    circularShift(arr, 5); 
    return 0;
}
