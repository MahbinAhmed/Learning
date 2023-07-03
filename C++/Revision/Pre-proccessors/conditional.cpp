#include<iostream>
using namespace std;

#define PI 3.1416
#define g 9.8

int main(){
    cout<<"Value of PI -> "<<PI<<endl;
    #if defined PI
    #undef g
    #endif
    // cout<<"Value of PI -> "<<PI<<endl;

    // #ifdef PI
    // cout<<"PI is defined"<<endl;
    // #else
    // cout<<"PI is not defined"<<endl;
    // #endif

    // #ifndef PI
    // cout<<"PI is not defined"<<endl;
    // #else
    // cout<<"PI is defined"<<endl;
    // #endif

    // #if not defined PI
    #if defined g
    cout<<"Value of g -> "<<g<<endl;
    #elif defined PI
    cout<<"Value of PI -> "<<PI<<endl;
    #else
    cout<<"NONE of them are declared"<<endl;
    #endif
    return 0;
}