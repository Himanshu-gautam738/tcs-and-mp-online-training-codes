#include <stdio.h>
#include <stdlib.h>

void printMatrix(int **mat, int rows, int cols) {
    printf("\nMatrix:\n");
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            printf("%d ", *(*(mat + i) + j)); 
        }
        printf("\n");
    }
}

int main() {
    int rows = 3, cols = 3;
    int **matrix;
    matrix = (int**) malloc(rows * sizeof(int*));
    for(int i = 0; i < rows; i++) {
        matrix[i] = (int*) malloc(cols * sizeof(int));
    }
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            *(*(matrix + i) + j) = (i + 1) * (j + 2);
        }
    }
    printMatrix(matrix, rows, cols);
    for(int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}
