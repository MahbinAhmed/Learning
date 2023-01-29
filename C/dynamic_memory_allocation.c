#include<stdio.h>
#include<stdlib.h>

int main()
{
    // <---MALLOC FUNCTION--->

    // int *ptr;
    // int n,i;

    // n = 5;
    // ptr = (int*) malloc(n*sizeof(int));
    // if(ptr==NULL){
    //     printf("Memory allocation failed!.\n");
    // }
    // else{
    //     printf("Memory allocation successfull using malloc function!\n");
    //     for(i=0;i<n;i++){
    //         ptr[i] = i+1;
    //     }
    //     printf("Elements are:- ");
    //     for(i=0;i<n+9;i++){
    //         printf("%d,",ptr[i]);
    //     }
    // }

    // <---CALLOC FUNCTION--->

    int *ptr;
    int n,i;

    n = 5;
    ptr = (int*) calloc(n, sizeof(int));
    if(ptr==NULL){
        printf("Memory allocation failed!.\n");
    }
    else{
        printf("Memory allocation successfull using calloc function!\n");
        for(i=0;i<n;i++){
            ptr[i] = i+1;
        }

        printf("Elements are:- ");
        // free(ptr);
        // ptr = NULL;

        // ptr = (int*) realloc(ptr, 7*sizeof(int));
        // ptr[5] = 6;
        // ptr[6] = 7;
        // ptr[7] = 8;
        // free(ptr);
        ptr = NULL;
        for(i=0;i<n+3;i++){
            printf("%d,",ptr[i]);
        }
    }
    // printf("%d",ptr);
}