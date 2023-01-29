#include<stdio.h>
#include "temp.c"
int sum=60;
int func(int a,int b){
    int sum;
    sum = a+b;
    return sum;
}

int main(){
    int result = func(3,5);
    printf("%d",sum);
}