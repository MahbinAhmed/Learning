#include<stdio.h>
#include "temp.c"
#define PI 3.14
#define square(r) r*r

int main(){
    // printf("The value of sum is %d\n", sum);
    printf("The value of PI is %f\n",PI);
    printf("The are of the circle is %f\n",PI*square(4));
}