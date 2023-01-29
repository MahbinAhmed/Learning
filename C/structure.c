#include<stdio.h>
#include<string.h>
struct Student
{
    char name[50];
    int id;
    int mark;
};

int main()
{
    struct Student s1;
    strcpy(s1.name,"Programming boy");
    s1.id = 508;
    s1.mark = 440;
    struct Student s2;
    s2.id = 509;
    s2.mark = 349;
    // printf("%s",s1.name);
    printf("%d",s2.id);
    
}