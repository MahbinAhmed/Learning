#include<iostream>
using namespace std;

int c = 50;

int main(){
    // <<<<<---Built-in Data Types--->>>>>
    // int a=5,b=10;
    // int c = a+b;
    // cout<<"The value of C is "<<c<<endl;
    // cout<<"The value of Global C is "<<::c<<endl; /*:: is used to print global variable from a function*/

    // <<<<<---float, double, long double Literals--->>>>>
    // float d=34.4F;
    // long double e = 34.4L; 
    // cout<<"The size of 34.4 is "<<sizeof(34.4)<<endl; /*Normally compiler denotes fraction number as double*//
    // cout<<"The size of 34.4f is "<<sizeof(34.4f)<<endl;
    // cout<<"The size of 34.4F is "<<sizeof(34.4F)<<endl;
    // cout<<"The size of 34.4l is "<<sizeof(34.4l)<<endl;
    // cout<<"The size of 34.4L is "<<sizeof(34.4L)<<endl;
    // cout<<"The value of d is "<<d<<endl<<"The value of e is "<<e;  

    // <<<<<---Reference Variable--->>>
    // int x = 560;
    // int &y = x;
    // cout<<x<<endl;
    // cout<<y<<endl;

    // <<<<<---Typecasting--->>>>>
    int a = 45;   
    float b = 45.46;
    cout<<"The value of a is "<<(float)a<<endl;
    cout<<"The value of a is "<<float(a)<<endl;

    cout<<"The value of b is "<<(int)b<<endl;
    cout<<"The value of b is "<<int(b)<<endl;
    int c = int(b);

    cout<<"The expression is "<<a + b<<endl;
    cout<<"The expression is "<<a + int(b)<<endl;
    cout<<"The expression is "<<a + (int)b<<endl;


    return 0;
}