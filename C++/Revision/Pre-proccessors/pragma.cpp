#include<iostream>
using namespace std;

void hello(){
    cout<<"Hello"<<endl;
}

void hi(){
    cout<<"Hi"<<endl;
}

/*
#pragma startup hello
#pragma exit hi

These won't work in gcc compilers. Instead we need to use ('__attribute__' function used below) to get the same result.
*/

void __attribute__((constructor)) hello();
void __attribute__((destructor)) hi();

int main(){
    hello();
    hi();
    cout<<"From main function()"<<endl;
    return 0;
}