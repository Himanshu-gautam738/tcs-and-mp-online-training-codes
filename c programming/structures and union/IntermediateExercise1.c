#include <stdio.h>
#include <string.h>
int i;
struct contect
{
    char name[30];
    char phone[30];
    char email[30];
};

int main()
{
    int n ;
    printf("enter number :");
    scanf("%d",&n);
    getchar();
    struct contect c[3];
    FILE *fptr;
    getchar;
    for (i = 0; i < n; i++)
    {
        printf("enter name :");
        fgets(c[i].name,sizeof(c[i].name),stdin);
        c[i].name[strcspn(c[i].name,"\n")]='\0';
        printf("enter phone :");
        fgets(c[i].phone,sizeof(c[i].phone),stdin);
        c[i].phone[strcspn(c[i].phone,"\n")]='\0';
        printf("enter email :");
        fgets(c[i].email,sizeof(c[i].email),stdin);
        c[i].email[strcspn(c[i].email,"\n")]='\0';
    }

    fptr=fopen("contect.dat","wb");
    fwrite(c,sizeof(struct contect),n,fptr);
    fclose(fptr);
    fptr=fopen("contect.dat","rb");
    fread(c,sizeof(struct contect),n,fptr);
    fclose(fptr);
    for (i = 0; i < n; i++)
    {
        printf("name :%s\n", c[i].name);
        printf("phone :%s\n", c[i].phone);
        printf("email :%s\n", c[i].email);
    }
}