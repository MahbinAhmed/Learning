#include <iostream>
using namespace std;

class Base
{
public:
    int base = 5;
    virtual void get_data()
    {
        cout << "Base(From Base Class):- " << base << endl;
    }
};
class Derived : public Base
{
public:
    int derived = 10;
    void get_data()
    {
        cout << "Base(From Derived Class):- " << base << endl;
        cout << "Derived(From Derived Class):- " << derived << endl;
    }
};

int main()
{
    Base o1;
    Derived o2;
    Base *bptr = &o2;
    bptr->get_data();
    return 0;
}