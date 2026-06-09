#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student
{
    int id;
    char name[50];
    float grade;
    int numCourses;
    char courses[10][50];
};

union Course
{
    char courseName[50];
};

void addStudent(struct Student students[], int *count);
void displayStudents(struct Student students[], int count);
void saveToFile(struct Student students[], int count);
void loadFromFile(struct Student students[], int *count);

int main()
{
    struct Student students[100];
    int count = 0;
    int choice;

    loadFromFile(students, &count);

    do
    {
        printf("\nStudent Data Management System\n");
        printf("1. Add Student\n");
        printf("2. Display All Students\n");
        printf("3. Save & Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar();

        switch (choice)
        {
        case 1:
            addStudent(students, &count);
            break;
        case 2:
            displayStudents(students, count);
            break;
        case 3:
            saveToFile(students, count);
            printf("Data saved. Exiting...\n");
            break;
        default:
            printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}

void addStudent(struct Student students[], int *count)
{
    struct Student s;
    union Course c;

    printf("\nEnter Student ID: ");
    scanf("%d", &s.id);
    getchar();

    printf("Enter Student Name: ");
    fgets(s.name, sizeof(s.name), stdin);
    s.name[strcspn(s.name, "\n")] = 0;

    printf("Enter Grade: ");
    scanf("%f", &s.grade);
    getchar();

    printf("How many courses ");
    scanf("%d", &s.numCourses);
    getchar();

    for (int i = 0; i < s.numCourses; i++)
    {
        printf("Enter Course %d name: ", i + 1);
        fgets(c.courseName, sizeof(c.courseName), stdin);
        c.courseName[strcspn(c.courseName, "\n")] = 0;
        strcpy(s.courses[i], c.courseName);
    }
    students[*count] = s;
    (*count)++;

    printf("Student added successfully!\n");
}
void displayStudents(struct Student students[], int count)
{
    if (count == 0)
    {
        printf("No student records found!\n");
        return;
    }
    printf("Student Records");
    for (int i = 0; i < count; i++)
    {
        printf("\nStudent ID: %d\n", students[i].id);
        printf("Name: %s\n", students[i].name);
        printf("Grade: %.2f\n", students[i].grade);
        printf("Courses:\n");
        for (int j = 0; j < students[i].numCourses; j++)
        {
            printf("  - %s\n", students[i].courses[j]);
        }
    }
}
void saveToFile(struct Student students[], int count)
{
    FILE *fp = fopen("students.bin", "wb");
    if (fp == NULL)
    {
        printf("Error opening file for writing!\n");
        return;
    }
    fwrite(&count, sizeof(int), 1, fp);
    fwrite(students, sizeof(struct Student), count, fp);
    fclose(fp);
}
void loadFromFile(struct Student students[], int *count)
{
    FILE *fp = fopen("students.bin", "rb");
    if (fp == NULL)
        return;
    fread(count, sizeof(int), 1, fp);
    fread(students, sizeof(struct Student), *count, fp);
    fclose(fp);
}
