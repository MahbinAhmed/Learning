#include<stdio.h>
int main(){
    int a = 50;
    switch (a)
    {
    case 20:
        printf("The value of a is 20\n");
        // break;
    case 50:
        printf("The value of a is 50\n");
        // break;
    case 10:
        printf("The value of a is 10\n");
        break;

    default:
        printf("This line is printed from default option");
        break;
    }
}