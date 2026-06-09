#include <stdio.h>
#include <string.h>
int i;
struct student
{
    int rollno;
    char name[30];
    float marks;
};

void sortStudents(struct student s[], int n)
{
    int j;
    struct student temp;
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (s[i].marks < s[j].marks)  
            {
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
}

void printdec(struct student s[],int n){
     printf("\noutput of structure :\n");
    for (i = 0; i < n; i++)
    {
        printf("rollno :%d\n", s[i].rollno);
        printf("name :%s\n", s[i].name);
        printf("marks :%f\n", s[i].marks);
    }
}

int main()
{
    int n;
    struct student s[20];
    printf("enter number :");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("enter rollno:");
        scanf("%d", &s[i].rollno);
        printf("enter name:");
        scanf("%s", s[i].name);
        printf("enter marks:");
        scanf("%f", &s[i].marks);
    }
    sortStudents(s, n);
    printdec(s,n);
   
}