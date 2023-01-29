// #include<stdio.h>
// void change_value(int *a){
//     *a = 10;
// }
// int main()
// {
//     int a = 5;
//     printf("The value of a before function call is : %d\n",a);
//     change_value(&a);
//     printf("The value of a after function call is : %d\n", a);

// }


// Quick quiz

#include<stdio.h>
void new_value(int*a,int*b){
    int add = *a + *b;
    int sub = *a - *b;
    *a = add;
    *b = sub;
}
int main()
{
    int a = 4,b = 3;
    printf("Values before function call:- a = %d, b = %d\n",a,b);
    new_value(&a,&b);
    printf("Values after function call:- a = %d, b = %d",a,b);
}