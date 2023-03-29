#include <iostream>
using namespace std;

class Base
{
public:
    int base;
    void get_data()
    {
        cout << "Base(From Base Class):- " << base << endl;
    }
};

class Derived : public Base
{
public:
    int derived;
    void get_data()
    {
        cout << "Base(From Derived Class):- " << base << endl;
        cout << "Derived:- " << derived << endl;
    }
};

int main()
{
    Base o1;
    Derived o2;
    Base *bptr = &o2; // Base class pointer pointing to Derived class object
    // (*bptr).derived = 50; //This will show an error because the pointer is made from Base class and can't access Derived class variable
    // (*bptr).get_data();

    bptr->base = 23;
    bptr->get_data();

    Derived *dptr = &o2; // Derived class pointer pointing to Derived class object
    dptr->base = 34;
    dptr->derived = 94;
    dptr->get_data();

    return 0;
}