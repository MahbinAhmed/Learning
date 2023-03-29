#include <iostream>
using namespace std;

int count = 0;

class A
{
public:
    A()
    {
        count++;
        cout << "Object " << count << " created successfully!" << endl;
    }
    ~A()
    {
        cout << "Object " << count << " destroyed successfully!" << endl;
    }
};

int main()
{
    A o1;
    {
        A o2;
    }
    return 0;
}