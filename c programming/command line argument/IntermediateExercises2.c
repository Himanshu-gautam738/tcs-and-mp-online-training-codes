#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    FILE *fp;
    char word[50];
    int count = 0;
    if (argc != 3) {
        printf("Use: %s <filename> <searchword>\n", argv[0]);
        return 1;
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("File not found!\n");
        return 1;
    }
    while (fscanf(fp, "%s", word) == 1) {
        if (strcasecmp(word, argv[2]) == 0) 
            count++;
    }
    fclose(fp);

    printf("The word '%s' appears %d times.\n", argv[2], count);

    return 0;
}
