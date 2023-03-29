#include <iostream>
using namespace std;

class Base
{
protected:
    int a = 10;

public:
    virtual void get_data() = 0;
};

class Derived : public Base
{
public:
    void get_data()
    {
        cout << "Value of a(From Derived Class):- " << a << endl;
    }
};

int main()
{
    Derived o1;
    Base *ptr = &o1;
    ptr->get_data();
    return 0;
}