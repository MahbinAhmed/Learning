#include <iostream>
using namespace std;

class math
{
    int a;
    int b;

public:
    int set_data(int x, int y)
    {
        a = x;
        b = y;
    }
    int set_data_with_sum(math x, math y)
    {
        a = x.a + y.a;
        b = x.b + y.b;
    }
    int get_data()
    {
        cout << "a = " << a << " b = " << b << endl;
    }
};

int main()
{
    math m1, m2, m3;
    m1.set_data(2, 5);
    m1.get_data();

    m2.set_data(6, 4);
    m2.get_data();

    m3.set_data_with_sum(m1, m2);
    m3.get_data();
    return 0;
}