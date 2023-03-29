#include <iostream>
using namespace std;

template <class T = int>
class A
{
    T a;

public:
    A(T x)
    {
        a = x;
    }

    void get_data()
    {
        cout << "The value of a is:- " << a << endl;
    }
};

int main()
{
    A<> o1(5.365);
    o1.get_data();
    return 0;
}