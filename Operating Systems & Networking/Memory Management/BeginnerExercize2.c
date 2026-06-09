#include <stdio.h>

int main() {
    int ref[] = {1, 3, 0, 3, 5, 6, 3};
    int frames[3] = {-1, -1, -1};
    int front = 0, faults = 0;

    for(int i = 0; i < 7; i++) {
        int found = 0;

        for(int j = 0; j < 3; j++) {
            if(frames[j] == ref[i]) {
                found = 1;
                break;
            }
        }

        if(!found) {
            frames[front] = ref[i];
            front = (front + 1) % 3;
            faults++;
        }

        printf("Frames: ");
        for(int j = 0; j < 3; j++) {
            printf("%d ", frames[j]);
        }
        printf("\n");
    }

    printf("Total Page Faults: %d\n", faults);

    return 0;
}