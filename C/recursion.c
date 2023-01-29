#include<stdio.h>
int factorial(int n);
int main()
{
    int factorial_result;
    factorial_result = factorial(20);
    printf("The result is %d", factorial_result);
}
int factorial(int n){
    if (n==1){
        return 1;
    }
    else if(n==0){
        return 0;
    }
    else{
        return n * factorial(n-1);
    }
}