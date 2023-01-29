#include<stdio.h>

int sum(int a, int b){
    return a+b;
}
void greet(){
    printf("Welcome to the program!\n");
}
int main(){
    // int (*fptr)(int,int);
    // fptr = &sum;
    // int result = (*fptr)(5,6);
    // printf("Your result is %d\n",result);

    /*IN A WRONG WAY*/
    // int (*fptr)(int,int);
    // fptr = &greet();

    void (*ptr)();
    ptr = &greet;
    // (*ptr)();
    ptr();
}