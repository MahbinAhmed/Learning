#include <iostream>
using namespace std;

class complex
{
    int a;
    int b;
    friend complex friend_func(complex x, complex y);

public:
    void set_data(int x, int y)
    {
        a = x;
        b = y;
    }
    void get_data()
    {
        cout << "a = " << a << " | b = " << b << endl;
    }
};

complex friend_func(complex x, complex y)
{
    complex z;
    z.set_data((x.a + y.a), (x.b + y.b));
    return z;
}

int main()
{
    complex c1, c2, c3;
    c1.set_data(4, 5);
    c1.get_data();
    c2.set_data(7, 4);
    c2.get_data();
    c3 = friend_func(c1, c2);
    c3.get_data();
    return 0;
}