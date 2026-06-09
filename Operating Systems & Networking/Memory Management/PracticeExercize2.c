#include <stdio.h>

void firstFit(int blocks[], int m, int processes[], int n) {
    int allocation[n];
    int frag = 0;

    for (int i = 0; i < n; i++) allocation[i] = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (blocks[j] >= processes[i]) {
                allocation[i] = j;
                frag += blocks[j] - processes[i];
                blocks[j] = 0;
                break;
            }
        }
    }

    printf("First Fit:\n");
    for (int i = 0; i < n; i++) {
        printf("P%d -> Block %d\n", i, allocation[i]);
    }
    printf("Fragmentation: %d\n\n", frag);
}

void bestFit(int blocks[], int m, int processes[], int n) {
    int allocation[n];
    int frag = 0;

    for (int i = 0; i < n; i++) allocation[i] = -1;

    for (int i = 0; i < n; i++) {
        int best = -1;
        for (int j = 0; j < m; j++) {
            if (blocks[j] >= processes[i]) {
                if (best == -1 || blocks[j] < blocks[best]) {
                    best = j;
                }
            }
        }

        if (best != -1) {
            allocation[i] = best;
            frag += blocks[best] - processes[i];
            blocks[best] = 0;
        }
    }

    printf("Best Fit:\n");
    for (int i = 0; i < n; i++) {
        printf("P%d -> Block %d\n", i, allocation[i]);
    }
    printf("Fragmentation: %d\n");
}

int main() {
    int blocks1[] = {100, 500, 200, 300, 600};
    int blocks2[] = {100, 500, 200, 300, 600};
    int processes[] = {212, 417, 112, 426};

    int m = 5, n = 4;

    firstFit(blocks1, m, processes, n);
    bestFit(blocks2, m, processes, n);

    return 0;
}