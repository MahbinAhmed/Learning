#include<iostream>
using namespace std;

int factorial(int n){
    if (n<=1){
        return 1;
    }
    return n* factorial(n-1);
}

int fib(int n){
    if (n<=1){
        return 1;
    }
    return fib(n-2) + fib(n-1);
}

int main(){
    int a=10;
    int b;
    cout<<"Factorial of "<<a<<" is "<<factorial(a)<<endl;
    cout<<"Enter a number to get fib value:- ";
    cin>>b;
    cout<<"The "<<b<<"th term of fibonacchi series is "<<fib(b)<<endl;
    return 0;
}