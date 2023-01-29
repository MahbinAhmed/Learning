#include<stdio.h>

typedef struct Student{
    int marks;
} std;

int main(){
    typedef int inte;
    inte a=5;
    // printf("%d\n",a);
    std s1;
    s1.marks = 500;
    printf("Marks:- %d\n",s1.marks);
    int *x,*b;
    int c=4;
    x = &c;
    b = &c;
}