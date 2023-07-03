#include<stdio.h>

int add(int a,int b){
    return a+b;
}

int main(){
    int (*p)(int, int);
    p = &add;
    int r = p(2,3);
    printf("%d\n", r);
    return 0;
}