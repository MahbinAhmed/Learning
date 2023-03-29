#include <iostream>
using namespace std;

class A
{
    int a;
    int b;

public:
    void set_data(int x, int y)
    {
        a = x;
        b = y;
    }
    void get_data()
    {
        cout << "The value of a is:- " << a << endl;
        cout << "The value of b is:- " << b << endl;
    }
};

int main()
{
    // A o1;
    // A *ptr = &o1;

    // (*ptr).set_data(3,76);
    // (*ptr).get_data();

    // A *ptr = new A;
    // ptr->set_data(5,3);
    // ptr->get_data();

    A *ptr = new A[3];
    ptr->set_data(23, 4);
    ptr->get_data();
    (ptr + 1)->set_data(32, 45);
    (ptr + 1)->get_data();
    return 0;
}