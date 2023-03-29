#include<iostream>
#include<iomanip> /*To use setw(n) manipulator*/
using namespace std;

int main(){
    // Constant in C++
    // const int a = 5;
    // cout<<"The value of a is "<<a<<endl;
    // int a = 10; /*This will throw an error because the variable is a constant*/

    // Manipulators in C++
    // int a=3, b=78, c=1549;
    // cout<<"The value of a is "<<setw(4)<<a<<endl;
    // cout<<"The value of b is "<<setw(4)<<b<<endl;
    // cout<<"The value of c is "<<setw(4)<<c<<endl;

    // Operator Precedence
    int a=3, b=4;
    int c = ((((a*5)+b)-45)+87);
    cout<<c;
    return 0;
}