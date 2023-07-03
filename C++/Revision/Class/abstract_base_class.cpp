#include<iostream>
using std::cout;
using std::endl;

class ABS_Class{
    virtual void pure_base_class()=0;
};

class Derived: public ABS_Class{
    public:
    Derived(){}
    void pure_base_class(){
        int a = 5;
    }
    void greet(){
        cout<<"Good Morning!"<<endl;
    }
};

int main(){
    Derived o1;
    ABS_Class *ptr;
    ptr = &o1;

    return 0;
}