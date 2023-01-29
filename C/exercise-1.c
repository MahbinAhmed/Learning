//Multiplication table of number entered by user

// #include<stdio.h>
// int main()
// {
//     int user_input;
//     printf("Enter number to print multiplication table:- ");
//     scanf("%d", &user_input);
//     printf("%d * 1 = %d\n", user_input,user_input*1);
//     printf("%d * 2 = %d\n", user_input,user_input*2);
//     printf("%d * 3 = %d\n", user_input,user_input*3);
//     printf("%d * 4 = %d\n", user_input,user_input*4);
//     printf("%d * 5 = %d\n", user_input,user_input*5);
//     printf("%d * 6 = %d\n", user_input,user_input*6);
//     printf("%d * 7 = %d\n", user_input,user_input*7);
//     printf("%d * 8 = %d\n", user_input,user_input*8);
//     printf("%d * 9 = %d\n", user_input,user_input*9);
//     printf("%d * 10 = %d\n", user_input,user_input*10);
//     return 0;
// }

#include<stdio.h>
int main()
{
    int input;
    printf("Which number's multiplication table do you want? :- ");
    scanf("%d", &input);
    for (int i=1; i<=10;i++){
        printf("%d * %d = %d\n", input, i, input*i);
    }
}