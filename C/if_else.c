#include<stdio.h>
int main()
{
    int input;
    printf("Please enter your age:- ");
    scanf("%d", &input);
    if (input>=18){
        printf("You are 18 or greater than that!");
    }
    else if(input>=10){
        printf("You are between 10 and 18");
    }
    else{
        // if (input<=4){
        //     printf("You are lesser than 4!");
        // }
        // else{
        //     printf("You are greater than 4 but not than 10");
        // }
        printf("Hello World");
    }
}