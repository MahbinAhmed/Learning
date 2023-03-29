#include <iostream>
using namespace std;

class PC
{
protected:
    int ram;

public:
    PC(int x) : ram(x) {}
    virtual void get_data()
    {
        cout << endl
             << "NULL" << endl;
    }
};

class Laptop : public PC
{
protected:
    int serial_no;
    int camera_resulation;

public:
    Laptop(int x, int s, int c) : PC(x)
    {
        serial_no = s;
        camera_resulation = c;
    }

    void get_data()
    {
        cout << "Laptop Specification:-" << endl;
        cout << "Serial No.:- " << serial_no << endl;
        cout << "Display size:- " << camera_resulation << " MP" << endl;
        cout << "Ram:- " << ram << " GB" << endl;
        cout << endl;
    }
};

class Desktop : public PC
{
protected:
    int chipset_no;
    int monitor_size;

public:
    Desktop(int x, int c, int m) : PC(x)
    {
        chipset_no = c;
        monitor_size = m;
    }

    // void get_data(){
    //     cout<<"Desktop Specification:-"<<endl;
    //     cout<<"Motherboard Chipset No.:- "<<chipset_no<<endl;
    //     cout<<"Monitor size:- "<<monitor_size<<" inch"<<endl;
    //     cout<<"Ram:- "<<ram<<" GB"<<endl;
    //     cout<<endl;
    // }
};

int main()
{
    Laptop o1(8, 342343, 20);
    Desktop o2(8, 81, 21);
    PC *lptr;
    PC *dptr;
    lptr = &o1;
    dptr = &o2;
    lptr->get_data();
    dptr->get_data();
    return 0;
}