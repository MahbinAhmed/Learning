#include<iostream>
using namespace std;

class Student{
    private:
    int a,b,c;
    public:
    int d,e;
    void set_data(int x, int y, int z);
    void get_data(){
        cout<<"The value of a "<<a<<endl;
        cout<<"The value of b "<<b<<endl;
        cout<<"The value of c "<<c<<endl;
        cout<<"The value of d "<<d<<endl;
        cout<<"The value of e "<<e<<endl;
    }
};

void Student::set_data(int x, int y, int z){
    a = x;
    b = y;
    c = z;
}

int main(){
    Student John;
    John.d = 45;
    John.e = 34;
    // John.a = 49; This will throw an error because a is a private variable
    John.set_data(23,43,5);
    John.get_data();
    return 0;
}