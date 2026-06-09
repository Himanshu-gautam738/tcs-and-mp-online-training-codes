#include <stdio.h>
void secondLargest(int arr[])
{
    int i;
    int max, second;
    max = arr[0];
    for (i = 1; i < 5; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    second = arr[0];
    for (i = 0; i < 5; i++)
    {
        if (arr[i] != max && arr[i] > second)
        {
            second = arr[i];
        }
    }
    printf("Second largest number is: %d", second);
}

int main()
{
    int arr[5], i;
    printf("Enter 5 array elements:\n");
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }
    secondLargest(arr);
    return 0;
}
