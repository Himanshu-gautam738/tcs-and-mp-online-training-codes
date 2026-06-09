#include <stdio.h>

int main() {
    int pages[] = {2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5};
    int frames[3] = {-1, -1, -1};
    int recent[3] = {0, 0, 0};
    int faults = 0, time = 0;

    for (int i = 0; i < 11; i++) {
        int page = pages[i];
        int found = 0;

        for (int j = 0; j < 3; j++) {
            if (frames[j] == page) {
                found = 1;
                recent[j] = time;
                break;
            }
        }

        if (!found) {
            faults++;

            int lru_index = 0;
            for (int j = 1; j < 3; j++) {
                if (recent[j] < recent[lru_index]) {
                    lru_index = j;
                }
            }

            frames[lru_index] = page;
            recent[lru_index] = time;
        }

        time++;

        printf("Frames: ");
        for (int j = 0; j < 3; j++) {
            printf("%d ", frames[j]);
        }
        printf("\n");
    }

    printf("Total Page Faults: %d\n", faults);

    return 0;
}