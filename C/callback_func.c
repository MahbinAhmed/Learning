#include<stdio.h>

int sum(int a,int b){
    return a+b;
}

int greet(int(*ptr)(int,int)){
    printf("Hello World!\n");
    // printf("The result is %d\n", ptr(4,6)); //It's also a valid code without (* )
    printf("The result is %d\n", (*ptr)(4,6));
}

int main(){
    int (*fptr)(int,int);
    fptr = sum;
    greet(fptr);
    // greet(sum);
}