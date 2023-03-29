#include <iostream>
using namespace std;

class A
{
public:
    int a;
    int b;
    A(int x, int y) : a(x), b(y)
    {
        cout << "Object constructed successfully!" << endl;
        cout << "Value of a is:- " << a << endl;
        cout << "Value of b is:- " << b << endl;
    }
};

int main()
{
    A o1(5, 309);
    return 0;
}