#include<iostream>
#include<string>
using namespace std;

class Binary{
    string s;
    void bin_check();
    public:
    void input();
    void display(){
        cout<<"You entered"<<endl;
        cout<<s<<endl;
    }
    void opposite();
};

void Binary :: input(){
    cout<<"Enter the binary number:- "<<endl;
    cin>>s;
}

void Binary :: bin_check(){
    for(int i=0; i<s.length();i++){
        if(s.at(i)!='1' && s.at(i)!='0'){
            cout<<"This is not a binary number!"<<endl;
            exit(0);
        }
    }
}

void Binary :: opposite(){
    bin_check();
    for (int i=0;i<s.length();i++){
        if(s.at(i)=='0'){
            s.at(i)='1';
        }
        else{
            s.at(i)='0';
        }
    }
    cout<<"Binary number after making opposite:-"<<endl;
    cout<<s;
}

int main(){
    Binary a;
    a.input();
    a.display();
    // a.bin_check();
    a.opposite();
    return 0;
}