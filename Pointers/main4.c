#include<stdio.h>

// Call by value | Call by reference

int increase(int *a){
    return *a = *a + 1;
}

int main(){
    int a=10;
    increase(&a);
    printf("%d\n", a);
    return 0;
}