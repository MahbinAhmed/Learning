#include<stdio.h>
void arrayReversal(int arr[])
{
    int i,temp;
    for (i=0;i<7/2;i++){
        temp = arr[i];
        arr[i] = arr[6-i];
        arr[6-i] = temp;
    }
}

void arrayPrint(int arr[])
{
    int i;
    for (i=0;i<7;i++){
        printf("Value of index %d is %d\n",i,arr[i]);
    }
}

int main()
{
    int array[] = {3,4,45,43,54,6,45};
    printf("Array before reversal:- \n");
    arrayPrint(array);
    arrayReversal(array);
    printf("Array after reversal:- \n");
    arrayPrint(array);
}