#include<stdio.h>
#include<stdlib.h>

int *add(int *a, int *b){
    // int c = (*a)+(*b); 
    int *c = (int*)malloc(sizeof(int));
    *c = (*a)+(*b);
    return c;
}

int main(){
    int a=2, b=5;
    int *c = add(&a,&b);
    printf("%d\n",*c);
    // printf("%d\n",c);
    return 0;
}