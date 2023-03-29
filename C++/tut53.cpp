#include <iostream>
using namespace std;

class A
{
    int a;

public:
    void set_data(int a)
    {
        this->a = a;
    }

    void get_data()
    {
        cout << "The value of a is:- " << a << endl;
    }
};

int main()
{
    A o1;
    o1.set_data(5);
    o1.get_data();
    return 0;
}