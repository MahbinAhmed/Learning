#include<iostream>
using namespace std;

struct student{
    int id;
    char grade;
    float mark;
}stdn;

typedef union employee{
    int id;
    float salary;
    char car;
}emp;

int main(){
    enum Meal{breakfast, lunch, dinner};
    Meal m1 = lunch;
    cout<<m1;
    struct student John;
    John.id=345;
    John.grade='x';
    John.mark=504.54;
    // cout<<John.id<<endl;
    // cout<<John.grade<<endl;
    // cout<<John.mark<<endl;

    emp Alex;
    Alex.id = 545;
    Alex.car = 'c';
    // cout<<Alex.car<<endl;
}