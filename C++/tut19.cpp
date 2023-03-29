#include<iostream>
using namespace std;

int sum(int a, int b){
    return a+b;
}

int sum(int a, int b, int c){
    return a+b+c;
}

int main(){
    cout<<"The sum of 5 and 10 is "<<sum(5,10)<<endl;
    cout<<"The sum of 5, 10 and 20 is "<<sum(5,10,20)<<endl;
    return 0;
}