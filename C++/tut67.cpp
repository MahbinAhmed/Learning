#include <iostream>
using namespace std;

template <class T>
void var_swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

int main()
{
    char a = 'x';
    char b = 'y';
    var_swap(a, b);
    cout << a << endl;
    cout << b << endl;
    return 0;
}