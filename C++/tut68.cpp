#include <iostream>
using namespace std;

template <class T>
void func(T x)
{
    cout << "This is from templatised function:- " << x << endl;
}

void func(int x)
{
    cout << "This is from non-templatised function:- " << x << endl;
}

int main()
{
    func(5);
    func(5.32);
    func('5');
    return 0;
}