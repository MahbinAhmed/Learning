#include <iostream>
using namespace std;

class A
{
    int a;

public:
    void set_data(int x = 20)
    {
        a = x;
    }

    void get_data()
    {
        cout << "a = " << a << endl;
    }
};

int main()
{
    A o1;
    o1.set_data();
    o1.get_data();
    return 0;
}