#include <stdio.h>
#include <string.h>
int i;
struct student
{
    int rollno;
    char name[30];
    float marks;
    
};

int main()
{
    int n=3;
    struct student s[n];
    FILE *ptr;

    for ( i = 0; i < n; i++)
    {
        printf("enter rollno :");
        scanf("%d",&s[i].rollno);
        getchar();

        printf("enter name :");
        fgets(s[i].name,sizeof(s[i].name),stdin);
        s[i].name[strcspn(s[i].name,"\n")]='\0';

        printf("enter marks :");
        scanf("%f",&s[i].marks);
        getchar();
    }

    ptr=fopen("transaction.dat","wb");
    if (ptr==NULL)
    {
        printf("file error");
        return 0;
    }
    
    fwrite(s,sizeof(struct student),n,ptr);
    fclose(ptr);

    ptr=fopen("transaction.dat","rb");
    fread(s,sizeof(struct student),n,ptr);
    fclose(ptr);

    for (i = 0; i < n; i++)
    {

        printf("rollno :%d\n", s[i].rollno);
        printf("name :%s\n", s[i].name);
        printf("marks :%f\n", s[i].marks);
    }

}