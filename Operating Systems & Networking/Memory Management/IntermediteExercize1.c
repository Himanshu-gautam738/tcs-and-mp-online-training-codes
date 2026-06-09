#include <stdio.h>
#include <math.h>

int main() {
    int total = 512;
    int block = total;

    printf("Initial Memory: %dKB\n", total);

    // Allocate 128KB
    while (block > 128) {
        block = block / 2;
        printf("Split to %dKB blocks\n", block);
    }
    printf("Allocated 128KB\n");

    // Allocate 64KB
    int block2 = 128;
    while (block2 > 64) {
        block2 = block2 / 2;
        printf("Split to %dKB blocks\n", block2);
    }
    printf("Allocated 64KB\n");

    // Deallocate
    printf("Deallocating 64KB and merging...\n");
    block2 = block2 * 2;
    printf("Merged to %dKB\n", block2);

    printf("Deallocating 128KB and merging...\n");
    block = block * 2;
    printf("Merged to %dKB\n", block);

    return 0;
}