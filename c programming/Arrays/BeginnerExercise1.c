/*Write a C program that takes an array of integers as input and
finds the smallest element using a function.*/

#include <stdio.h>
int arrminprint(int arr[])
{
    int i;
    int max = arr[0];
    for (i = 1; i <= 5; i++)
    {
        if (max > arr[i])
        {
            max = arr[i];
        }
    }
    printf("minimum number is  :%d", max);
}
int main()
{
    int arr[5], i;
    printf("enter an arrays :");
    for (i = 0; i <5; i++)
    {
        scanf("%d", &arr[i]);
    }
    arrminprint(arr);
    
}
