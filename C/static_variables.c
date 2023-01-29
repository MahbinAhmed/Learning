#include<stdio.h>
int func(){
    static int value=5;
    value++;
    return value;
}
int main()
{
    int a = func(); 
    printf("%d\n",a);
    a = func(); 
    printf("%d",a);
}