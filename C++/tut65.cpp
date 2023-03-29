#include <iostream>
using namespace std;

template <class T, class U>
class A
{
    T a;
    U b;

public:
    A(T x, U y)
    {
        a = x;
        b = y;
    }

    void get_data()
    {
        cout << a << endl
             << b << endl;
    }
};

int main()
{
    A<int, float> o1(5, 4.2);
    // A <int, float> *ptr = &o1;
    // ptr ->get_data();
    o1.get_data();
    return 0;
}