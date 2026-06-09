#include <stdio.h>
#include <stdlib.h>
int* allocate() {
    int *ptr = (int*) malloc(sizeof(int));   
    if (ptr == NULL) {                 //memory is allocated or not       
        printf("Memory allocation failed!\n");
        exit(1);
    }
    *ptr = 5;                                
    return ptr;                          
}
int main() {
    int *a = allocate(); 
    printf("Value: %d\n", *a);
    free(a);                             //Memory loss here is because free() was not invoked
    a = NULL;         
    a = allocate();        
    printf("Value again: %d\n", *a);
    free(a);             
    a = NULL;
    return 0;
}
