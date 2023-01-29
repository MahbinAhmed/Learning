#include<stdio.h>
int sum(int a, int b);
void printStar();
int main()
{
    int a,b;
    a = 6;
    b = 549;
    int result = sum(a,b);
    // printf("The result is %d",result);
    printStar(5);
}

int sum(int a, int b)
{
    return a+b;
}
void printStar(int n)
{
    int i;
    for (i=0;i<n;i++){
    printf("*");
    }
}