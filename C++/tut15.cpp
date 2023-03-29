#include<iostream>
using namespace std;

int sum(int, int);

int main(){
    int num1, num2;
    cout<<"Enter the value of num1 "<<endl;
    cin>>num1;
    cout<<"Enter the value of num2 "<<endl;
    cin>>num2;

    cout<<"The sum of num1 and num2 is "<<sum(num1, num2); /*Here num1 and num2 are actual parameters.*/
    return 0;
}

int sum(int a, int b){ /*Here a and b are formal paramters*/
    return a+b;
}