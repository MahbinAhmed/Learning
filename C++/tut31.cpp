#include <iostream>
using namespace std;

class X
{
    int a;
    int b;
    int c;

public:
    X()
    {
        a = 0;
        b = 0;
        c = 0;
    }

    X(int inp1)
    {
        a = inp1;
        b = 0;
        c = 0;
    }

    X(int inp1, int inp2, int inp3)
    {
        a = inp1;
        b = inp2;
        c = inp3;
    }

    void get_data()
    {
        cout << "a = " << a << " | b = " << b << " | c = " << c << endl;
    }
};

int main()
{
    X o1, o2(5), o3(8, 38, 564);
    o1.get_data();
    o2.get_data();
    o3.get_data();
    return 0;
}