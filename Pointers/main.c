#include<stdio.h>

int main(){
    int a=10;
    int *p = &a;

    // printf("%d\n", p);
    // printf("%d\n", &a);
    // printf("%d\n", *p);

    printf("Address of a:- %d\n", &a);
    printf("Address of value p:- %d\n", p);
    printf("Address of pointer p:- %d\n", &p);
    printf("Size of integer:- %d\n", sizeof(int));
    // printf("Address of (pointer+1):- %d\n", &(p+1)); //Error
    printf("Address of (pointer+1):- %d\n", p+1);
    return 0;
}