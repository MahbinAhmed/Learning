#include <iostream>
using namespace std;

class base1
{
    int a;

public:
    base1(int x)
    {
        a = x;
        cout << "Base 1 class created successfully!" << endl;
    }
    void get_data_base1()
    {
        cout << "Value of a from base 1 class:- " << a << endl;
    }
};

class base2
{
    int b;

public:
    base2(int y)
    {
        b = y;
        cout << "Base 2 class created successfully!" << endl;
    }
    void get_data_base2()
    {
        cout << "Value of b from base 2 class:- " << b << endl;
    }
};

class derived : public base2, virtual public base1
{
    int c, d;

public:
    derived(int p, int q, int r, int s) : base1(r), base2(s)
    {
        c = p;
        d = q;
        cout << "Derived class created successfully!" << endl;
    }
    void get_data_derived()
    {
        cout << "Value of c from derived class:- " << c << endl;
        cout << "Value of d from derived class:- " << d << endl;
    }
};

int main()
{
    derived o1(5, 20, 15, 21);
    o1.get_data_base1();
    o1.get_data_base2();
    o1.get_data_derived();
    return 0;
}