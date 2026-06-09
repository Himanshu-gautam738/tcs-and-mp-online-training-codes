#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd = open("data.txt", O_RDWR);
    int size = 100;

    char *mapped = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

    strcpy(mapped, "Hello from mmap!");

    printf("File Content: %s\n", mapped);

    munmap(mapped, size);
    close(fd);

    return 0;
}