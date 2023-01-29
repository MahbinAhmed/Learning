#include<stdio.h>
typedef struct Student
{
    int id;
    int mark;
} Std;

int main()
{
    typedef int integer;
    struct Student s1;
    s1.id = 5093;
    s1.mark = 459;
    printf("Mark of Student 1 (Id: %d) is %d\n",s1.id,s1.mark);
    Std s2;
    s2.id = 5409;
    s2.mark = 394;
    printf("Mark of Student 2 (Id: %d) is %d\n",s2.id,s2.mark);
    integer a = 5;
    printf("Value of a is %d\n",a);
}