#include <stdio.h>
#include <string.h>
union Student
{
    int id;
    int mark;
    char name[34];
};

void main()
{
    union Student s1;
    strcpy(s1.name,"Student 1");
    s1.mark = 34;
    s1.id = 4590;

    printf("Id = %d\n",s1.id);
    printf("Mark = %d\n",s1.mark);
    printf("Name = ");
    printf(s1.name);
}