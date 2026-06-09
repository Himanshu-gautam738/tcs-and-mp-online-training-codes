/*Develop a menu-driven program that allows users to:
1. Check if a number is prime
2. Generate Fibonacci series upto n terms
3. Check if a number is palindrome
4. Exit the program*/

// print prime number
#include <stdio.h>
int prime(int n)
{
   int i;
   if (i <= 1)
   {
      printf("number is not prime");
      return 0;
   }
   for (i = 2; i <= n / 2; i++)
   {
      if (n % i == 0)
      {
         printf("number is not prime: %d\n", n);
         return 0;
      }
      else
      {
         printf("number is prime :%d\n", n);
         return 0;
      }
   }
}

// print fibonacci series
void fibo(int n)
{
   int a = 0, b = 1, c, i;

   printf("Fibonacci series: ");

   for (i = 0; i < n; i++)
   {
      printf("%d\n", a);
      c = a + b;
      a = b;
      b = c;
   }
}

// print palindrome of numbers
void palindrome(int n)
{
   int temp, rev = 0, digit;
   temp = n;
   while (n > 0)
   {
      digit = n % 10;
      rev = rev * 10 + digit;
      n = n / 10;
   }
   if (temp == rev)
   {
      printf("number is palindrom :%d\n", temp);
   }
   else
   {
      printf("number is not palindrom :%d\n", temp);
   }
}

int main()
{
   int n, choise;
   printf("enter a number :");
   scanf("%d", &n);
   do
   {
      printf("choise 1 number is prime:\n");
      printf("choise 2 number of Fibonacci series:\n");
      printf("choise 3 number is palindrome :\n");
      printf("choise 4 Exit:\n");
      printf("Exit\n");
      printf("enter your choise :");
      scanf("%d", &choise);
      switch (choise)
      {
      case 1:
         prime(n);
         break;
      case 2:
         fibo(n);
         break;
      case 3:
         palindrome(n);
         break;
      case 4:
         printf("Exiting program.\n");
         break;

      default:
         printf("default value");
         break;
      }
   } while (choise != 4);
   return 0;
}
