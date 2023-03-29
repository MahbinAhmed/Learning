#include <iostream>
using namespace std;

class A
{
public:
    int adata;
    int id = 550;
    A() {}
    A(int x)
    {
        adata = x;
        id = 1001;
    }
    void set_id()
    {
        id = 220;
    }
    void get_data()
    {
        cout << "From class A: adata = " << adata << endl;
    }
};

class B : public A
{
public:
    int bdata;
    B(int y)
    {
        bdata = y;
    }
    void get_id()
    {
        cout << id << endl;
    }
    // B(){}
};

int main()
{
    A o1(5);
    B o2(45);
    o1.get_data();
    // o2.get_id(); //This statement is needed to get id if the derived class is in private mode
    o2.set_id();
    cout << o2.id << endl;
    return 0;
}