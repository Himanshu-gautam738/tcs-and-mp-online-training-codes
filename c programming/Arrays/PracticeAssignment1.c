#include <stdio.h>

int findMax(int arr[], int n) {
    int max = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] > max)
            max = arr[i];
    }
    return max;
}

int findMin(int arr[], int n) {
    int min = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] < min)
            min = arr[i];
    }
    return min;
}

// Function to find sum of array
int findSum(int arr[], int n) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

// Function to find average of array
float findAverage(int arr[], int n) {
    int sum = findSum(arr, n);
    return (float)sum / n;
}

// Function to perform binary search
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(arr[mid] == key)
            return mid;
        else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;  // element not found
}

// Function to reverse an array
void reverseArray(int arr[], int n) {
    int start = 0, end = n - 1;
    while(start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}


void bubbleSort(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        int swapped = 0;
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = 1;
            }
        }
        if(swapped == 0)
            break;
    }
}

// Function to print array
void printArray(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int n, key, choice;
    
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);
    
    int arr[n];
    
    printf("Enter %d elements of the array:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    do {
        printf("1. Display Array\n");
        printf("2. Find Maximum Element\n");
        printf("3. Find Minimum Element\n");
        printf("4. Find Sum of Elements\n");
        printf("5. Find Average of Elements\n");
        printf("6. Binary Search an Element\n");
        printf("7. Reverse Array\n");
        printf("8. Sort Array (Bubble Sort)\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1:
                printf("Array elements: ");
                printArray(arr, n);
                break;
            case 2:
                printf("Maximum element: %d\n", findMax(arr, n));
                break;
            case 3:
                printf("Minimum element: %d\n", findMin(arr, n));
                break;
            case 4:
                printf("Sum of array elements: %d\n", findSum(arr, n));
                break;
            case 5:
                printf("Average of array elements: %.2f\n", findAverage(arr, n));
                break;
            case 6:
                printf("Enter element to search: ");
                scanf("%d", &key);
                bubbleSort(arr, n); // Sorting before binary search
                int index = binarySearch(arr, n, key);
                if(index != -1)
                    printf("Element %d found at position %d (0-based indexing)\n", key, index);
                else
                    printf("Element %d not found in the array.\n", key);
                break;
            case 7:
                reverseArray(arr, n);
                printf("Array after reversing: ");
                printArray(arr, n);
                break;
            case 8:
                bubbleSort(arr, n);
                printf("Array after sorting: ");
                printArray(arr, n);
                break;
            case 0:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice! Try again.\n");
        }
    } while(choice != 0);
    
    return 0;
}
