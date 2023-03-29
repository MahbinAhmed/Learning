#include <iostream>
using namespace std;

class Base
{
protected:
    int a = 10;

private:
    int b;
};

class Derived : protected Base
{
public:
    void get_protected_data()
    {
        // cout<<b<<endl; //This will give an error as b is a private member
        cout << a << endl;
    }
};

int main()
{
    Derived o1;
    o1.get_protected_data();
    return 0;
}