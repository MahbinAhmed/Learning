#include<stdio.h>

int compare(int a, int b){
    if(a>b) return 1;
    else return 0;
}

void bubble_sort(int arr[], int n,int (*comp)(int, int)){
    for(int i=0;i<n;i++){
        for(int j=i;j<n-1;j++){
            if(comp(arr[j],arr[j+1])>0){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main(){
    int A[5] = {3,42,6,4,5};
    int n = 5;
    int (*comp)(int, int) = &compare;
    bubble_sort(A, 5, comp);
    for(int i=0;i<n;i++){
        printf("%d ",A[i]);
    }
    return 0;
}