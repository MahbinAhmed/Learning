#include<stdio.h>
int main(){
    int a =10;
    int *ptr;
    // *ptr = 34; Not recommended to use
    ptr = &a; //It's no longer remains as a wild pointer
    printf("The value is %d", *ptr);
}