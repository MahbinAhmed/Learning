#include <iostream>
using namespace std;

class Base1
{
protected:
    int a;

public:
    void set_val1(int x)
    {
        a = x;
    }
};

class Base2
{
protected:
    int b;

public:
    void set_val2(int y)
    {
        b = y;
    }
};

class Derived : public Base1, public Base2
{
public:
    void get_val()
    {
        cout << "Value from base 1:- " << a << endl;
        cout << "Value from base 2:- " << b << endl;
        cout << "Sum of values:- " << a + b << endl;
    }
};

int main()
{
    Derived o1;
    o1.set_val1(50);
    o1.set_val2(34);
    o1.get_val();
    return 0;
}