#include<iostream>
using namespace std;

int main(){
    for (int i=0; i<=5;i++){
        if(i==1){
            continue;
        }
        cout<<i<<endl;
        if(i==3){
            break;
        }
    }
}