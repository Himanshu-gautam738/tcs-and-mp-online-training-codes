#include<stdio.h>
#include<string.h>

struct student
{
    char name[30];
    int rollno;
    float marks;
};

void update(struct student *c){
    c->marks=95;
}

int main(){
    struct student st={"himanshu",101,92};
    update(&st);
    printf("name :%s\n",st.name);
    printf("rollno :%d\n",st.rollno);
    printf("rollno :%f\n",st.marks);

}