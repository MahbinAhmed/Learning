#include<stdio.h>
void func(int array[])
{
    array[2]=10;
    printf("In-function: Value of 1th element in the list:- %d\n", (array+3));
}
void func_ref(int *array)
{
    printf("In-function: Value of 0th element in the list:- %d\n", array[0]);
    // printf("In-function: Value of 0th element in the list:- %d\n", array);
    printf("In-function: Value of 1th element in the list:- %d\n", *(array+1));
    *(array+1)=10;
}
int main()
{
    int arr[] = {3,5,45,6};
    printf("%d\n",arr[2]);
    func(arr);
    printf("%d",arr[2]);
    // func_ref(arr);
    // printf("%d",arr[1]);

}