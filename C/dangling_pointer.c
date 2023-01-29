#include<stdio.h>
#include<stdlib.h>

// // Cause-1: Deallocation of memory
// int main(){
//     int a = 10;
//     int *ptr = (int*) malloc(sizeof(int));
//     *ptr = a;
//     printf("First print %d\n",ptr);
//     printf("First value print %d\n", *ptr);
//     free(ptr);
//     printf("Second print %d\n",ptr);
//     printf("Second value print %d\n", *ptr);
//     ptr = NULL;
//     printf("Third print %d\n",ptr);
//     printf("Third value print %d\n",*ptr);
// }

// // Cause-2: Returning local variable in function calls
// int *sample(){
//     int a=10;
//     return &a;
// }
// int main(){
//     int *ptr = sample();
//     printf("The pointer address is %d\n", ptr);
// }

// Cause-3: Variable going out of the scope [NB. It's not a dangling pointer. It works perfectly.]
int main(){
    int *ptr;
    {
        int a = 10;
        ptr = &a;
        printf("Printing from inside of the scope %d\n", *ptr);
    }
    printf("Printing from outside of the scope %d\n", *ptr);
}