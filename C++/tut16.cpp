#include<iostream>
using namespace std;

// Call by value
void swap_with_value(int a, int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

// Call by referrence
void swap_with_pointer(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

// With referrence variable
void swap_with_refVer(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main(){
    int a=10;
    int b=5;
    cout<<"a = "<<a<<", b = "<<b<<endl;
    swap_with_value(a,b);
    cout<<"After swaping with \"swap_with_value\" funciton"<<endl;
    cout<<"a = "<<a<<", b = "<<b<<endl;
    swap_with_pointer(&a, &b);
    cout<<"After swaping with \"swap_with_pointer\" function"<<endl;
    cout<<"a = "<<a<<", b = "<<b<<endl;
    a = 10; b = 5;
    cout<<"Value reseted\n";
    cout<<"After swaping with \"swap_with_refVar\" function"<<endl;
    swap_with_refVer(a,b);
    cout<<"a = "<<a<<", b = "<<b<<endl;
}