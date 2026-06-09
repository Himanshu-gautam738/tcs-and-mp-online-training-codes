#include <stdio.h>
#include <string.h>
struct Owner
{
    int rollno;
    char name[30];
    float percentage;
    
};
union owner
{ 
    int rollno;
    char name[30];
    float percentage;
};
int main()
{
printf("----This is structure ----\n");
    struct Owner s1={101,"Himanshu",92.5};
    struct Owner s2={102,"Hari",98};
    struct Owner s3={103,"Aman",96.5};
    printf("%d %s %f \n",s1.rollno,s1.name,s1.percentage);
    printf("%d %s %f \n",s2.rollno,s2.name,s2.percentage);
    printf("%d %s %f \n\n",s3.rollno,s3.name,s3.percentage);
    
printf("----This is union----\n");
    union owner u1;
    u1.rollno=101;
    printf("%d \n",u1.rollno);
    strcpy(u1.name,"himanshu");
    printf("%s \n",u1.name);
    u1.percentage=93.5;
    printf("%f \n",u1.percentage);

    printf("size of structure is :%lu \n",sizeof(struct Owner));
    printf("size of union is :%lu",sizeof(union owner));
}