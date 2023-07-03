#include<stdio.h>

int main(){
    // // Two-Dimensional Arrays
    // int a[2][3] = {{4,5,6},{3,2,7}};
    // // int a[3] = {3,2,7};
    // printf("%d\n", *a);
    // printf("%d\n", a[0]);
    // printf("%d\n", &a[0][0]);
    // printf("%d\n", *(a[0]+1));
    // printf("%d\n", *((a+1)+1));

    // Three-Dimensional Arrays
    int a[3][2][2] = {{{5,7},{9,2}},{{3,4},{1,8}},{{6,3},{7,2}}};
    int (*p)[2][2] = a;
    printf("%d\n", *(*(*(p+1))));
    return 0;
}