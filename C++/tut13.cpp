#include<iostream>
using namespace std;

int main(){
    // Arrays
    int mark[5] = {45,23,54,56,43};
    // cout<<mark[2]<<endl;
    // cout<<"Printing array with for loop:- "<<endl;
    // for(int i=0;i<5;i++){
    //     cout<<mark[i]<<endl;
    // }

    // Pointer with Arrays
    int *ptr = mark;
    // cout<<ptr[0]<<endl;
    // ptr++;
    // cout<<*(ptr+1)<<endl;
    for(int i=0;i<5;i++){
        cout<<*(ptr+i)<<endl;
    }
    return 0;
}