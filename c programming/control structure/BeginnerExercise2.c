/*Calculate the sum of numbers from 1 to N using a for loop. */
#include<stdio.h>
int main(){
    int sum=0,i,n;
    printf("enter number :");
    scanf("%d",&n);
    for ( i = 0; i <=n; i++)
    {
        sum+=i;
    }
    printf("sum of numbers is:%d",sum);
}