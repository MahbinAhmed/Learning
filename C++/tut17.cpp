#include<iostream>
using namespace std;

inline int sum(const int a,int b){
    return a+b;
}

int study_time(int days, int hours_per_day = 5){
    return days*hours_per_day;
}

int main(){
    int a=5;
    int b=10;
    cout<<"The sum os 5 and 10 is "<<sum(a,b)<<endl;
    cout<<"For normal students "<<study_time(10)<<" hours"<<endl;
    cout<<"For good students "<<study_time(10,6)<<" hours"<<endl;
    return 0;
}