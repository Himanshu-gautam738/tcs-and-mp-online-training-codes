#include <stdio.h>
#define GRID_SIZE 5
int main()
{
    int row = 2, col = 2;
    char directions[] = {'U', 'D', 'L', 'R', 'U'};
    int steps[] = {2, 1, 3, 1, 1};
    for(int i=0;i<5;i++){
        int newrow=row;
        int newcol=col;
        switch (directions[i]){
            case 'U':
            newrow-=steps[i];
            break;
            case 'D':
            newrow+=steps[i];
            break;
            case 'L':
            newcol-=steps[i];
            break;
            case 'R':
            newcol+=steps[i];
            break;

        }
        if(newrow>=0 && newrow <GRID_SIZE && newcol>=0 && GRID_SIZE){
            row=newrow;
            col=newcol;
        }
    }
    printf("final position (%d,%d)\n",row ,col);
}