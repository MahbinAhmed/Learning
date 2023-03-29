#include<iostream>
using namespace std;
int global = 10;

int sum(){
    cout<<global;
}

int main(){
    int a=5;
    int b=6;
    float pi=3.14;
    int global = 20;

    cout<<"The value of a is "<<a<<". The value of b is "<<b<<".\n The value of pi is "<<pi<<"\n";
    cout<<global;
    return 0;
}