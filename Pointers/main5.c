#include<stdio.h>

int array_sum(int *a, int size){
    int sum = 0;
    for(int i=0;i<size;i++){
        sum += a[i];
    }
    return sum;
}

int main(){
    int arr[] = {2,4,5,3,9};
    int *p = arr;
    int i = 2;
    // printf("%d\n",arr);
    // printf("%d\n",&arr);
    // printf("%d\n",p);

    // printf("%d\n",&arr[i]);
    // printf("%d\n",arr+i);
    // printf("%d\n",p+i);
    int size = sizeof(arr)/sizeof(arr[0]);
    int sum = array_sum(arr, size);
    printf("%d\n",sum);
    return 0;
}