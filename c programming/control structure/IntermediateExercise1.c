/*Write a program that generates and displays the multiplication table for a
number entered by the user using a for loop.*/

#include<stdio.h>
int main(){
    int i,n;
    printf("enter number :");
    scanf("%d",&n);
    for ( i = 1; i <= 10; i++)
    {
        printf("%d*%d=%d\n",n,i,n*i);
    }
    
}
