#include <iostream>
using namespace std;

class Base
{
    int val1;

public:
    int val2;
    void set_data()
    {
        val1 = 5;
        val2 = 10;
    }
    int get_val1()
    {
        return val1;
    }
    int get_val2()
    {
        return val2;
    }
};

class Derived : public Base
{
    int val3;

public:
    void start()
    {
        val3 = val2 * get_val1();
    }
    void get_data()
    {
        cout << "val1 = " << get_val1() << endl;
        cout << "val2 = " << val2 << endl;
        cout << "val3 = " << val3 << endl;
    }
};

int main()
{
    Derived o1;
    o1.set_data();
    o1.start();
    o1.get_data();
    return 0;
}