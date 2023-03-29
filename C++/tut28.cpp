#include <iostream>
using namespace std;

class Second;
class First
{
    int a;

public:
    friend void swap(First &, Second &);
    void set_data(int x)
    {
        a = x;
    }

    void get_data()
    {
        cout << "a = " << a << endl;
    }
};

class Second
{
    int b;

public:
    friend void swap(First &, Second &);
    void set_data(int x)
    {
        b = x;
    }

    void get_data()
    {
        cout << "b = " << b << endl;
    }
};

void swap(First &x, Second &y)
{
    int temp = x.a;
    x.a = y.b;
    y.b = temp;
}

int main()
{
    First o1;
    Second o2;
    o1.set_data(5);
    o2.set_data(10);
    swap(o1, o2);
    o1.get_data();
    o2.get_data();
    return 0;
}