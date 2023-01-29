#include<stdio.h>

// union Student
// {
//     int roll;
//     int id;
//     int marks;
// };

union Size
{
    // int x;
    double y;
    char name[20];
};


int main(){
    // union Student s1;
    // s1.id = 5;
    // s1.roll = 1;
    // s1.marks = 599;
    // printf("Value is %d\n",s1.id);
    // printf("Value is %d\n",s1.roll);
    // printf("Value is %d\n",s1.marks);
    union Size s1;
    printf("%d\n",sizeof(s1));
}