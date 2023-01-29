#include<stdio.h>
int main()
{
    int input,index = 0;
    printf("Enter your number:- ");
    scanf("%d", &input);
    do
    {
        printf("%d\n",index+1);
        index = index + 1;
    }while(index < input);
}