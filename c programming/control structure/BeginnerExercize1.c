/*Write a C program to find the LCM of two numbers and then verify
it by listing several common multiples.*/

#include<stdio.h>
int main(){
   int a,b,i,n;
   int hcf=1,lcm;
   printf("enter a & b number :");
   scanf("%d %d",&a,&b);
   for (i = 1; i <=a && i<=b; i++)
   {
    if (a%i==0 && b%i==0)
    {
        hcf=i;
    }
   }
   lcm=(a*b)/hcf;
   printf(" lcm of number is :%d\n",lcm);
   printf("multiple of %d is :",a);
   for ( i = 1; i <= 5; i++)
   {
    printf("%d\t",a*i);
   }
   printf("\n");
   printf("multiple of %d is :",b);
   for ( i = 1; i <= 5; i++)
   {
    printf("%d\t",b*i);
   }
   
}