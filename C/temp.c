#include <stdio.h>
char name[20] = "Mahid";
int rounds;
int sum = 10;
// double a;
int main2()
{

    while (1)
    {
        printf("How many rounds you want to play this game?[3-999] :- ");
        int a = scanf("%d", &rounds);
        if(a==1){
        getchar();
        if (rounds < 3 || rounds > 999)
        {
            printf("Please enter a number between 3 and 999!\n");
            continue;
        }
        else
        {
            break;
        }
        }
        else{
            printf("Please enter a number!\n");
            continue;
        }
    }
}