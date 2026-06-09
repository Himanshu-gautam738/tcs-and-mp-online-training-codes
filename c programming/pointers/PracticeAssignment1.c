#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr = NULL;
    int size = 0, capacity = 5;
    int choice, value, i, pos;

    arr = (int *)malloc(capacity * sizeof(int));
    if (arr == NULL)
    {
        printf("Memory allocation failed!\n");
        return 1;
    }
    while (1)
    {
        printf("\n--- Dynamic Array Menu ---\n");
        printf("1. Add element\n");
        printf("2. Remove last element\n");
        printf("3. Display elements\n");
        printf("4. Search element\n");
        printf("5. Resize array\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            if (size == capacity)
            {
                capacity *= 2;
                arr = (int *)realloc(arr, capacity * sizeof(int));
                if (arr == NULL)
                {
                    printf("Memory reallocation failed!\n");
                    return 1;
                }
            }
            printf("Enter value to add: ");
            scanf("%d", &value);
            arr[size++] = value;
            printf("Element added!\n");
            break;
        case 2:
            if (size > 0)
            {
                size--;
                printf("Last element removed.\n");
            }
            else
            {
                printf("Array is empty.\n");
            }
            break;
        case 3:
            if (size == 0)
                printf("Array is empty.\n");
            else
            {
                printf("Array elements: ");
                for (i = 0; i < size; i++)
                    printf("%d ", arr[i]);
                printf("\n");
            }
            break;
        case 4:
            printf("Enter value to search: ");
            scanf("%d", &value);
            for (i = 0; i < size; i++)
            {
                if (arr[i] == value)
                {
                    printf("Element found at position %d.\n", i);
                    break;
                }
            }
            if (i == size)
                printf("Element not found.\n");
            break;
        case 5:
            printf("Enter new capacity: ");
            scanf("%d", &capacity);
            arr = (int *)realloc(arr, capacity * sizeof(int));
            if (arr == NULL)
            {
                printf("Memory resize failed!\n");
                return 1;
            }
            if (size > capacity)
                size = capacity;
            printf("Array resized to capacity %d.\n", capacity);
            break;
        case 6:
            free(arr);
            printf("Memory freed. Exiting...\n");
            return 0;
        default:
            printf("Invalid choice! Try again.\n");
        }
    }
}
