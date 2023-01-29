#include<stdio.h>
int main()
{
    int i,age;
    for (i=0;i<10;i++)
    {
        printf("Iteration no:- %d\n",i);
        printf("Please enter your age:- ");
        scanf("%d", &age);
        if (age<10)
        {
            printf("You are less than 10! So you are not eligable.\n");
            continue;
        }
        else if (age>18){
            printf("You are greater than 18! So you are terminated!\n");
            break;
        }
        else{
            printf("Congratulations!!! You are eligable for the contest!\n");
        }
        
    }
}