/*Create a program that prints the following pattern using nested for
loops: */

#include<stdio.h>
int main(){
    int i,n,j;
    printf("enter number :");
    scanf("%d",&n);
    for ( i = 1; i <= n; i++)
    {
       for ( j = 0; j <i; j++)
       {
        printf("*");
       }
       printf("\n");
       
    }
    
}
