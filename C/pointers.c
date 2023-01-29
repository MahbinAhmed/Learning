#include<stdio.h>
int sum(int *a, int size){
    int i, sum = 0;
    for (i=0;i<size;i++){
        sum = sum + *(a+i);
    }
    return sum;
}
int main()
{
    // int a=10;
    // int *p = &a;
    // int *np = NULL;
    // printf("%p\n",&a);
    // printf("%d\n", p);
    // printf("%p\n", *p);
    // printf("%p\n", &p);
    // printf("%d", np);
    int arr[3] = {4,5,10};
    int result = sum(arr, 3);
    printf("Sum of the array is :- %d",result);
}