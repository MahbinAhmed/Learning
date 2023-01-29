#include<stdio.h>
#include<string.h>
struct employee{
    char name[50];
    char role[20];
    int id;
    int salary;
}John;

int main(){
    struct employee alex;
    struct employee employer[2];
    strcpy(alex.name,"Al-Khan");
    John.id=54534;
    employer[1].id = 34534;
    employer[0].id = 3434984;
    printf("%s\n",alex.name);
    printf("%d\n",John.salary);
    printf("%d\n",John.id);
    printf("%d\n",employer[1].id);
    printf("%d\n",employer[0].id);
}