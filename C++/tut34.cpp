#include <iostream>
using namespace std;

class A
{
    int a;

public:
    A(int n)
    {
        a = n;
    }

    // If there's no copy constructer then compiler will supply it's own copy constructor
    A(A &n)
    {
        a = n.a;
    }

    void get_data()
    {
        cout << "a = " << a << endl;
    }
};

int main()
{
    A o1(5), o2(10), o3(o1), o4 = o2;
    o1.get_data();
    o2.get_data();
    o3.get_data();
    o4.get_data();
    return 0;
}