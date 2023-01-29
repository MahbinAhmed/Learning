#include<stdio.h>
int main(){
    int a = 10;
    float b = 30.5;
    void *ptr;
    ptr = &a;
    printf("The value of a is %d\n", (*(int*)ptr));
}