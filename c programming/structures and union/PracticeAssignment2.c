#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Employee {
    int id;
    char name[50];
    char designation[50];
    float salary;
};

union Salary {
    float monthly;
    float hourly;
};

void addEmployee(struct Employee emp[], int *count);
void displayEmployees(struct Employee emp[], int count);
void saveToFile(struct Employee emp[], int count);
void loadFromFile(struct Employee emp[], int *count);

int main() {
    struct Employee emp[100];
    int count = 0, choice;
    loadFromFile(emp, &count);

    do {
        printf("\n Employee Record Management System z\n");
        printf("1. Add Employee\n");
        printf("2. Display Employees\n");
        printf("3. Save & Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar();

        switch (choice) {
            case 1: addEmployee(emp, &count); break;
            case 2: displayEmployees(emp, count); break;
            case 3: saveToFile(emp, count);
                    printf("Data saved. Exiting...\n"); break;
            default: printf("Invalid choice! Try again.\n");
        }
    } while (choice != 3);
    return 0;
}

void addEmployee(struct Employee emp[], int *count) {
    struct Employee e;
    union Salary s;
    int type;

    printf("\nEnter Employee ID: ");
    scanf("%d", &e.id);
    getchar();

    printf("Enter Name: ");
    fgets(e.name, sizeof(e.name), stdin);
    e.name[strcspn(e.name, "\n")] = 0;

    printf("Enter Designation: ");
    fgets(e.designation, sizeof(e.designation), stdin);
    e.designation[strcspn(e.designation, "\n")] = 0;

    printf("Select Salary Type (1. Monthly / 2. Hourly): ");
    scanf("%d", &type);

    if (type == 1) {
        printf("Enter Monthly Salary: ");
        scanf("%f", &s.monthly);
        e.salary = s.monthly;
    } else {
        printf("Enter Hourly Salary: ");
        scanf("%f", &s.hourly);
        e.salary = s.hourly;
    }

    emp[*count] = e;
    (*count)++;
    printf("Employee added successfully!\n");
}
void displayEmployees(struct Employee emp[], int count) {
    if (count == 0) {
        printf("No employee records found!\n");
        return;
    }
    printf("\n--- Employee Records ---\n");
    for (int i = 0; i < count; i++) {
        printf("\nEmployee ID: %d\n", emp[i].id);
        printf("Name: %s\n", emp[i].name);
        printf("Designation: %s\n", emp[i].designation);
        printf("Salary: %.2f\n", emp[i].salary);
    }
}
void saveToFile(struct Employee emp[], int count) {
    FILE *fp = fopen("employees.bin", "wb");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fwrite(&count, sizeof(int), 1, fp);
    fwrite(emp, sizeof(struct Employee), count, fp);
    fclose(fp);
}
void loadFromFile(struct Employee emp[], int *count) {
    FILE *fp = fopen("employees.bin", "rb");
    if (fp == NULL) return;
    fread(count, sizeof(int), 1, fp);
    fread(emp, sizeof(struct Employee), *count, fp);
    fclose(fp);
}
