/*Write a C program that takes an array of integers as input and
reverses it using a function. */

#include <stdio.h>
void reversearry(int n)
{
   int arr[n],i;
   //input array element 
   printf("enter array  :");
   for (i = 0; i < n; i++)
   {
      scanf("%d", &arr[i]);
   }
   //print reverse array element
   printf("reverse of array is :");
   for (i = n - 1; i >= 0; i--)
   {
      printf("%d \n", arr[i]);
   }
}

int main()
{
   int n;
   printf("enter a number :");
   scanf("%d",&n);
   reversearry(n);
}
