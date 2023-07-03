#include<stdio.h>
#include<stdlib.h>

// Dynamic Memory Allocation

int main(){
    int *ptr,n;
    printf("Enter array size:- ");
    scanf("%d", &n);
    // ptr = (int *)malloc(n*sizeof(int)); // Using malloc function
    // for(int i=0;i<n;i++){
    //     ptr[i] = (i+1)*2;
    // }

    ptr = (int *)calloc(n,sizeof(int)); // Using calloc function
    for(int i=0;i<n;i++){
        ptr[i] = (i+1)*2;
    }

    // ptr = (int*)realloc(ptr,n*2*sizeof(int)); // Using realloc for reallocating space
    // ptr = (int*)realloc(NULL,n*2*sizeof(int)); // Using realloc as malloc function
    // ptr = (int*)realloc(ptr,0); // Using realloc as free function
    free(ptr); // Freeing the address pointer
    ptr = NULL; // Pointing the pointer to NULL
    for(int i=0;i<n*2;i++){
        printf("Array[%d] = %d\n",i+1, ptr[i]);
    }
    return 0;
}