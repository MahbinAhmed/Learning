#include<iostream>
using namespace std;

int main(){
    int a=5;
    int *b=&a;

    // & --->>> (Address of) operator
    // * --->>> (Value at) operator

    cout<<"The address of a is "<<&a<<endl;
    cout<<"The address of a is "<<b<<endl;
    cout<<"The value at address "<<b<<" is "<<*b<<endl;
    cout<<"The address of b is "<<&b<<endl;
    int **c = &b;
    cout<<**c<<endl;
}