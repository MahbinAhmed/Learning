#include <iostream>
using namespace std;

class Base1
{
public:
    int a = 5;
    void greet()
    {
        cout << "Hello World" << endl;
    }
};

class Base2
{
public:
    int a = 10;
    void greet()
    {
        cout << "Good Morning" << endl;
    }
};

class Derived : public Base1, public Base2
{
public:
    // int a = 20;
    using Base2 ::a;
    void greet()
    {
        Base2::greet();
        cout << "How are you?" << endl;
    }
};

int main()
{
    Derived o1;
    o1.greet();
    cout << o1.a << endl;
    return 0;
}