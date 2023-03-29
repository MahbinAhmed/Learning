// Exercise on C++ Inheritance
#include <iostream>
#include <cmath>
using namespace std;

class Normal_Calculator
{
public:
    void show_result(int result)
    {
        cout << "Your result is " << result << endl;
    }

    void add(int a, int b)
    {
        int result = a + b;
        show_result(result);
    }

    void sub(int a, int b)
    {
        int result = a - b;
        show_result(result);
    }

    void mul(int a, int b)
    {
        int result = a * b;
        show_result(result);
    }

    void div(int a, int b)
    {
        int result = a / b;
        show_result(result);
    }
};

class Scientific_Calculator
{
public:
    void show_result(int result)
    {
        cout << "Your result is " << result << endl;
    }
    void square(int x)
    {
        show_result(x * x);
    }

    void square_root(int x)
    {
        show_result(sqrt(x));
    }

    void power_of(int x, int y)
    {
        show_result(pow(x, y));
    }

    void logbase10(int x)
    {
        show_result(log10(x));
    }
};

class Hybrid_Calculator : public Normal_Calculator, public Scientific_Calculator
{
};

int main()
{
    Hybrid_Calculator o1;
    o1.add(20, 2);
    o1.sub(50, 20);
    o1.mul(5, 20);
    o1.div(50, 2);
    o1.square(4);
    o1.square_root(16);
    o1.power_of(4, 5);
    o1.logbase10(100);
    return 0;
}